# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 01:30:00 2021

@author: ShadabHussain
"""

import warnings 
warnings.filterwarnings("ignore")
import requests
import streamlit as st

# IBMQ
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, IBMQ
from qiskit.tools.monitor import job_monitor


st.set_page_config(page_title='QRNG', page_icon=None, layout='centered', initial_sidebar_state='auto')

st.markdown("<h1 style='text-align: center; color: black;'>Quantum Random Number Generator</h1>", unsafe_allow_html=True)

quantum_computer = st.sidebar.selectbox("Select Quantum Computer Type", ['IBMQ', 'ANU QRNG'])

subheader = "using "+ quantum_computer
st.markdown(f"<h1 style='text-align: center; color: black;'>{subheader}</h1>", unsafe_allow_html=True)


def about(quantum_computer):
    if quantum_computer == "ANU QRNG":
        text = "The Australian National University (ANU) offers true random numbers to anyone on the internet. The random numbers are generated in real-time in their lab by measuring the quantum fluctuations of the vacuum."
        link = 'https://qrng.anu.edu.au/contact/api-documentation/'
        link_text = 'For API Documentation'
    elif quantum_computer == "IBMQ":
        text = "Qiskit is an open source SDK for working with quantum computers at the level of pulses, circuits and application modules. It accelerates the development of quantum applications by providing the complete set of tools needed for interacting with quantum systems and simulators."
        link = 'https://qiskit.org/'
        link_text = 'For Qiskit Documentation'
    st.markdown(f"<body style='text-align: center; color: black;'>{text}</body>", unsafe_allow_html=True)
    st.markdown(f"<h4 align='center'> <a href={link}>{link_text}</a> </h4>", unsafe_allow_html=True)
        
    
about(quantum_computer)

def ibmq_qrng(minimum, maximum):
        
    q = QuantumRegister(num_q, 'q')
    c = ClassicalRegister(num_q, 'c')

    circuit = QuantumCircuit(q, c)
    circuit.h(q)  # Applies hadamard gate to all qubits
    circuit.measure(q, c)  # Measures all qubits

    job = execute(circuit, backend, shots=1)
    counts = job.result().get_counts()
    result = int(counts.most_frequent(), 2)
    result1 = minimum + result % (maximum+1 - minimum)
    return result1


def anu_generator(n, data_type):
    '''
    This function generates n random numbers between 0 and maxnum
    by calling Australian National University's API. 
    The reason why we're using this custom function instead of the 
    one built-in one is that ANU's numbers are generated in the
    university's lab by measuring the quantum fluctuations of the vacuum. 
    By doing so, we ensure true randomness.
    '''
    link_string = 'https://qrng.anu.edu.au/API/jsonI.php?length='+str(n)+'&type='+data_type.split(' ')[0]
    anu_data = requests.get(link_string).json()
    my_random_numbers = [0]*n
    for i in range(len(anu_data['data'])):
        my_random_numbers[i] = anu_data['data'][i]
    return(my_random_numbers)



if quantum_computer == "IBMQ":
    if quantum_computer == "IBMQ":
        try:
            IBMQ.load_account()
        except Exception as e:
            st.write(e)
            api_key = st.sidebar.text_input("Enter IBMQ API Key")
            IBMQ.save_account(api_key)
            IBMQ.load_account()
        provider = IBMQ.get_provider(hub='ibm-q')
        device = st.sidebar.selectbox("Select Quantum Device", [str(each) for each in provider.backends()])
        backend = provider.get_backend(device)
        if device == "ibmq_qasm_simulator":
            num_q = 32
        else:
            num_q = 5
    minimum = st.sidebar.number_input("Minimum Random Number", value=0)
    maximum = st.sidebar.number_input("Maximum Random Number", min_value=minimum+1, value=minimum+1)
elif quantum_computer == "ANU QRNG":
    data_type = st.sidebar.selectbox("Select Data Type", ['uint8 - integers between 0–255', 'uint16 - integers between 0–65535'])
    minimum = 0
    if 'uint8' in data_type:
        maximum = 255
    else:
        maximum = 65535
    st.sidebar.write("Minimum Random Number: ", minimum)
    st.sidebar.write("Maximum Random Number: ", maximum)

num_rand_numbers = st.sidebar.number_input("Number of Random Numbers to be Generated", min_value=1, value=1)

            
def display_result(result1):
    if 'result1' in locals():
        st.markdown(f"<h2 style='text-align: center; color: black;'>Sampling {num_rand_numbers} random number between {minimum} and {maximum}: {result1}</h2>", unsafe_allow_html=True)
    


if st.sidebar.button("Generate Random Number"):
    if num_rand_numbers <1:
        st.markdown(f"<h3 style='text-align: center; color: black;'>Please enter number of random numbers to be generated 1 or greater then 1</h3>", unsafe_allow_html=True)
    else:
        if quantum_computer == "IBMQ":
            if num_rand_numbers==1:
                result1 = ibmq_qrng(minimum, maximum)
            else:
                result1 = []
                for i in range(num_rand_numbers):
                    result1.append(ibmq_qrng(minimum, maximum))
            display_result(result1)
        elif quantum_computer == "ANU QRNG":
            display_result(anu_generator(num_rand_numbers, data_type))
else:
    st.markdown(f"<h3 style='text-align: center; color: black;'>Click on 'Generate Random Number' button</h3>", unsafe_allow_html=True)
