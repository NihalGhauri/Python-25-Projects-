import streamlit as st
import random
import time

def native_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0 
    if high is None:
        high = len(l) - 1
    
    while low <= high:
        midpoint = (low + high) // 2
        
        if l[midpoint] == target:
            return midpoint
        elif target < l[midpoint]:
            high = midpoint - 1
        else:
            low = midpoint + 1
    
    return -1

def generate_sorted_list(length):
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    return sorted(list(sorted_list))

def main():
    st.title('Binary Search vs Naive Search Comparison')

    col1, col2 = st.columns(2)

    with col1:
        list_length = st.slider('Select List Length', min_value=10, max_value=10000, value=1000)

    with col2:
        search_target = st.number_input('Enter Number to Search', value=7)

    if st.button('Perform Search'):
        sorted_list = generate_sorted_list(list_length)

        st.write(f"Generated list length: {len(sorted_list)}")
        st.write(f"Searching for: {search_target}")

        native_start = time.time()
        native_index = native_search(sorted_list, search_target)
        native_end = time.time()
        native_time = native_end - native_start

        binary_start = time.time()
        binary_index = binary_search(sorted_list, search_target)
        binary_end = time.time()
        binary_time = binary_end - binary_start

        st.subheader('Search Results')
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write('Naive Search:')
            st.write(f'Index: {native_index}')
            st.write(f'Time: {native_time:.9f} seconds')
        
        with col2:
            st.write('Binary Search:')
            st.write(f'Index: {binary_index}')
            st.write(f'Time: {binary_time:.9f} seconds')

        st.subheader('Performance Comparison')
        st.write(f'Naive Search Time: {native_time:.9f} seconds')
        st.write(f'Binary Search Time: {binary_time:.9f} seconds')
        
        speed_difference = native_time / binary_time if binary_time > 0 else 0
        st.write(f'Binary Search is approximately {speed_difference:.2f}x faster')

if __name__ == '__main__':
    main()