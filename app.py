from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "MyResume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Pradyumna Anil Kumar Kubear"
PAGE_ICON = ":wave:"
NAME = "Pradyumna Anil Kumar Kubear"
DESCRIPTION = """
Network Engineer with 3+ years of experience in CISCO Packet Tracer, GNS3, and Python development.
"""
EMAIL = "pradyumkubeara@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/pradyumna-anil-kumar-kubear-593903328/",
    "GitHub": "https://github.com/PradyumnaA",
}

# Projects with descriptions and links
PROJECTS = {
    "Phishing URL Generation": {
        "description": "► Generated Phishing URLs using GAN and detected Phishing URLs using Detectors.",
        "link": "https://NA"
    },
    "Transmission of Ping Messages": {
        "description": "► Implement transmission of ping messages/trace route over a network topology consisting of 6 nodes and find the number of packets dropped due to congestion",
        "link": "https://github.com/PradyumnaA/TransmissionOfPingMessages"
    },
    "GSM-CDMA": {
        "description": "► This script simulates a GSM network using NS2, configuring bandwidth, propagation delays, and queue limits for each link. TCP communication is established between two cell phones using FTP, and the results are logged in a trace file. The AWK script then processes this trace file to generate a graph showing the number of packets received over time.",
        "link": "https://github.com/PradyumnaA/GSM-CDMA"
    },
}

# --- SETUP PAGE ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 3+ years of experience in Network Engineering with Cisco Packet Tracer, GNS3, and NS2.
- ✔️ Hands-on experience in network protocols such as TCP/IP, UDP, DNS, DHCP, and more.
- ✔️ Skilled in programming with Python, and networking simulations with Packet Tracer, GNS3.
- ✔️ Experienced in working with REST APIs, and using Postman for API testing.
    """
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, REST API
- 🖧 Networking Protocols: TCP/IP, UDP, DNS, DHCP, SMTP, FTP
- 🖥️ Simulations: Packet Tracer, GNS3, NS2
- 🔧 Software: Postman, Cisco Packet Tracer, GNS3
    """
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1 ---
st.write("🚧", "**Teaching Assistant | University of the Pacific, Stockton, CA**")
st.write("01/2023 - 05/2024")
st.write(
    """
- ► Created assignments and quizzes on Access Control Lists, VPNs, and Firewalls.
- ► Evaluated students' Packet Tracer assignments and graded them.
    """
)

# --- JOB 2 ---
st.write('\n')
st.write("🚧", "**App Developer | Ambience Safety, Bengaluru, India**")
st.write("02/2022 - 07/2022")
st.write(
    """
- ► Network Configuration: Implemented real-time communications using protocols like TCP/UDP for messaging features.
- ► Service Integration: Configured and managed DNS for domain name resolutions and SMTP for email notifications to ensure reliable delivery of push notifications.
- ► Network Layer Optimization: Optimized app communication by configuring DHCP for dynamic IP addressing and ensured efficient traffic management with FTP for file transfers.
- ► End-to-End Testing: Performed endpoint testing of REST APIs, including connectivity testing of services that leveraged networking protocols (TCP/IP, DNS, FTP).
- ► System Integration: Integrated POP services for email retrieval functionalities within the app to manage notifications for users.
    """
)

# --- JOB 3 ---
st.write('\n')
st.write("🚧", "**Network Engineer | Syslog Technologies, Bengaluru, India**")
st.write("08/2020 - 12/2021")
st.write(
    """
- ► Resolved connectivity issues by configuring hubs, routers, and switches.
- ► Worked on IP addressing schemes and DHCP server configurations.
- ► Resolved network-related issues in developer forums and improved network performance.
    """
)

# --- INTERNSHIP ---
st.write('\n')
st.write("🚧", "**Intern | QSpiders, Bengaluru, India**")
st.write("07/2019 - 08/2019")
st.write(
    """
- ► Developed 'Network Simulations' using Cisco Packet Tracer, gaining hands-on experience in network configurations.
    """
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")

# Adding networking-themed emojis for each project
for project, details in PROJECTS.items():
    st.write(f"**🌐 [{project}]({details['link']})**")  # Networking icon added
    st.write(f"- {details['description']}")

# Adding subtle animations using Markdown for styling
st.markdown(
    """
    <style>
    @keyframes fadeIn { 
        from { opacity: 0; } 
        to { opacity: 1; } 
    }
    .stText { 
        animation: fadeIn ease 3s; 
    }
    </style>
    """, unsafe_allow_html=True
)
