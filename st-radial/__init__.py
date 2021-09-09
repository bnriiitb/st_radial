import os
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "st_radial",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("st_radial", path=build_dir)

def st_radial(title, value, start_angle=-135, end_angle=225, key=None):
    component_value = _component_func(title=title, value=value, start_angle=start_angle, end_angle=end_angle, key=key)
    return component_value

if not _RELEASE or __name__ == "__main__":
    import streamlit as st
    import random
    st.title('Streamlit Radial Test')
    cols = st.columns([.333,.333,.333])
    with cols[0]:
        st_radial('Metric 1', value=random.randrange(10, 100))
    with cols[1]:
        st_radial('Metric 2', value=random.randrange(10, 100))
    with cols[2]:
        st_radial('Metric 3', value=random.randrange(10, 100))