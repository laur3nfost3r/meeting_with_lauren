from manim import *
import streamlit as st

class CreateCircle(ThreeDScene):
    def construct(self):
        self.next_section("first section")
        axes = ThreeDAxes()
        circle = Circle()
        self.add(circle)
        self.wait(1)
        self.next_section("second section")
        self.add(axes)
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
        cylinder = Cylinder()
        self.play(Transform(circle,cylinder))
        self.wait()

st.title('Bare bones')
config.save_sections = True
c = CreateCircle()
c.render()
st.video("media/videos/1080p60/CreateCircle.mp4")
