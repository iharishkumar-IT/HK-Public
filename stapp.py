import streamlit as st

# Main Page
def main():
    st.title("Main Page")
    st.write("Welcome to the main page!")
    st.write("Use the links below to navigate to other pages:")
    
    st.markdown("[Go to Page 1](page1)", unsafe_allow_html=True)
    st.markdown("[Go to Page 2](page2)", unsafe_allow_html=True)
    st.markdown("[Go to Page 3](page3)", unsafe_allow_html=True)

# Page 1
def page1():
    st.title("Page 1")
    st.write("Welcome to Page 1!")
    st.markdown("[Go to Main Page](main)", unsafe_allow_html=True)
    st.markdown("[Go to Page 2](page2)", unsafe_allow_html=True)
    st.markdown("[Go to Page 3](page3)", unsafe_allow_html=True)

# Page 2
def page2():
    st.title("Page 2")
    st.write("Welcome to Page 2!")
    st.markdown("[Go to Main Page](main)", unsafe_allow_html=True)
    st.markdown("[Go to Page 1](page1)", unsafe_allow_html=True)
    st.markdown("[Go to Page 3](page3)", unsafe_allow_html=True)

# Page 3
def page3():
    st.title("Page 3")
    st.write("Welcome to Page 3!")
    st.markdown("[Go to Main Page](main)", unsafe_allow_html=True)
    st.markdown("[Go to Page 1](page1)", unsafe_allow_html=True)
    st.markdown("[Go to Page 2](page2)", unsafe_allow_html=True)

# Routing logic
def main_app():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Main", "Page 1", "Page 2", "Page 3"])

    if selection == "Main":
        main()
    elif selection == "Page 1":
        page1()
    elif selection == "Page 2":
        page2()
    elif selection == "Page 3":
        page3()

if __name__ == "__main__":
    main_app()
