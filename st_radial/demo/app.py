import streamlit as st

def about_dev():
    st.sidebar.title("About the developer")
    st.sidebar.markdown("""
    #### Hi there, I am Akshansh Kumar <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="25px">
    ###### Please visit my [github page](https://github.com/akshanshkmr) for more such utilities
    ###### If you liked my work and would like to support me, consider buying me a coffee 😄
    <br><a href="https://www.buymeacoffee.com/akshanshkmr" target="_blank">
    <img class="center" src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a> 
    """,unsafe_allow_html=True)

if __name__ == "__main__":
    about_dev()
    st.title('Streamlit Radial Demo')
    st.write('### Getting Started')
    with st.echo():
        from st_radial import st_radial
        import random
        cols = st.columns([.333,.333,.333])
        with cols[0]:
            st_radial('Metric 1', value=random.randrange(10, 100))
        with cols[1]:
            st_radial('Metric 2', value=random.randrange(10, 100))
        with cols[2]:
            st_radial('Metric 3', value=random.randrange(10, 100), start_angle=0)
