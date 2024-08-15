import streamlit as st
import base64

#needed images import 
def get_base64_image(image_path):
    """Encode an image as base64."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Paths to images
image_paths = {
    #"profile": "assets/profile_squared.png",
    #"logo": "assets/logo.png",
    #"background": "assets/background.jpg"
}

# Encoding images
encoded_images = {name: f"data:image/png;base64,{get_base64_image(path)}" for name, path in image_paths.items()}


def homepage():

    st.set_page_config(
        page_title = "Enyojo's Portfolio✮",
        page_icon = "🌸",
    )

    #css
    with open("assets/main.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    #st.image(encoded_images["logo"], caption="Logo")  # Display the logo image
    
     # Top title
    st.write(f"""<html><body class="is-preload"><div id="intro">
            <h2>Enyojo Alabi <br /> Portfolio </h2>
            <p>Hello, my name is Enyo✧, and  I am currently on a path of Data Science & Business Intelligence with previous experience in front-end developent and UI/UX design. Here are some of my projects ᵔᴗᵔ.</p>
            <ul class="actions">
                <li><a href="#header" class="button icon solid solo fa-arrow-down scrolly">Continue</a></li>
            </ul>
        </div></body></html>""", unsafe_allow_html=True)
    #header
    st.write(f'''
    <html><body class="is-preload">
    <header id="header">
            <a href="app.py" class="logo">Home ꕥ</a>
        </header></body></html>
    ''', unsafe_allow_html=True)

    #navigation bar
    st.write(f'''<html><body class="is-preload">
    <nav id="nav">
            <ul class="links">
                <li class="active"><a href="index.html">My Projects</a></li>
            </ul>
            <ul class="icons">
                <li><a href="https://www.linkedin.com/in/enyojo-alabi-48a971180" class="icon brands alt fa-linkedin"><span class="label">Linkedin</span></a></li>
                <li><a href="https://github.com/enyo-ojo" class="icon brands fa-github"><span class="label">GitHub</span></a></li>
            </ul>
        </nav>
        </body></html>
    ''', unsafe_allow_html=True)

    #top project
    st.write(f'''
    <html><body class="is-preload">
      <div id="main">
            <article class="post featured">
                <header class="major">
                    <span class="date">Jan, 2022</span>
                    <h2>
                        <a href="https://github.com/enyo-ojo/personaldashboard.github.io">Personalized Dashboard</a>
                    </h2>
                <p>This is a personalized web browser dashboard extension that opens up at the start of a browser <br /> The project was built using API's, JS, HTML and CSS
                    <br/> Click the title above to view code and below to view project</p>
            </header>
            <a href="#" class="image main"><img src="images/img14.png" alt="" /></a>
            <ul class="actions special">
                <li><a href="https://enyo-ojo.github.io/personaldashboard.github.io/" class="button large">View Project</a></li>
            </ul>
            </article></div</body></html>
    ''', unsafe_allow_html=True)

    #other projects list
    st.write(f'''
    <html><body class="is-preload">
      <div id="main">
           <section class="posts">
                <article>
                    <header>
                        <span class="date">2021</span>
                        <h2>
                            <a href="https://github.com/enyo-ojo/PACMAN-GAME">PACMAN GAME</a>
                        </h2>
                </header>
                <a href="#" class="image main"><img src="images/IMG1.png" alt="" /></a>
                <p>This is a pacman game that was built with CSS, HTML and JS
                    <br/> Click the title above to view code and below to view project</p>
                <ul class="actions special">
                    <li><a href="https://enyo-ojo.github.io/PACMAN-GAME.github.io/" class="button">View Project</a></li>
                </ul>
                </article>
                <article>
                    <header>
                        <span class="date">2022</span>
                        <h2><a href="https://github.com/enyo-ojo/Blog">Personal Blog<br />
                                     design</a></h2>
                    </header>
                    <a href="#" class="image fit"><img src="images/img6.png" alt="" /></a>
                    <p>Blog responsive design created with HTML and CSS. <br/> Click the title above to view code and below to view project</p>
                    <ul class="actions special">
                        <li><a href="https://enyo-ojo.github.io/Blogbyfibs.github.io/" class="button">View Project</a></li>
                    </ul>
                 </article>
                 <article>
                    <header>
                        <span class="date">2021</span>
                        <h2><a href="https://github.com/enyo-ojo/my-diary-app">Diary App</a></h2>
                    </header>
                    <a href="#" class="image fit"><img src="images/img3.png" alt="" /></a>
                    <p>Diary application design done with JS, CSS and HTML5 for a project in progress. <br/> Click the title above to view code and below to view project</p>
                    <ul class="actions special">
                        <li><a href="https://enyo-ojo.github.io/my-diary-app.github.io/" class="button">View Project</a></li>
                    </ul>
                </article>
                <article>
                    <header>
                        <span class="date">2021</span>
                        <h2><a href="https://github.com/enyo-ojo/fashionweb.github.io">fashion article<br />
										website</a></h2>
                    </header>
                    <a href="#" class="image fit"><img src="images/img11.png" alt="" /></a>
                    <p>A fashion article webpage design. Its responsive and built with html and css.<br/> Click the title above to view code and below to view project</p>
                    <ul class="actions special">
                        <li><a href="https://enyo-ojo.github.io/fashionweb.github.io/" class="button">view Project</a></li>
                    </ul>
                </article>
                <article>
                    <header>
                        <span class="date">2022</span>
                        <h2><a href="https://github.com/enyo-ojo/wargame.github.io">War Game<br />
										web app</a></h2>
                    </header>
                    <a href="#" class="image fit"><img src="images/img16.png" alt="" /></a>
                    <p>Game of war cards built with HTML,CSS, JS and APIs.<br/> Click the title above to view code and below to view project</p>
                    <ul class="actions special">
                        <li><a href="https://enyo-ojo.github.io/wargame.github.io/" class="button">view Project</a></li>
                    </ul>
                </article>
            <article>
                    <header>
                        <span class="date">2022</span>
                        <h2><a href="https://github.com/enyo-ojo/passwordgenerator.github.io">password generator</a></h2>
                    </header>
                    <a href="#" class="image fit"><img src="images/img12.png" alt="" /></a>
                    <p>A password generator web app that generates random passwords with <br/> Click the title above to view code and below to view project</p>
                    <ul class="actions special">
                        <li><a href="https://enyo-ojo.github.io/passwordgenerator.github.io/" class="button">view Project</a></li>
                    </ul>
                </article>
                <article>
                    <header>
                        <span class="date">2022</span>
                        <h2><a href="https://github.com/enyo-ojo/forestvacay.github.io">Forest Vacation <br />
                                     spots website</a></h2>
                    </header>
                    <a href="#" class="image fit"><img src="images/img13.png" alt="" /></a>
                    <p>Responsive website design for forest vacation bookings.<br/> Click the title above to view code and below to view project</p>
                    <ul class="actions special">
                        <li><a href="https://enyo-ojo.github.io/forestvacay.github.io/" class="button">view Project</a></li>
                    </ul>
                </article>
                <article>
                    <header>
                        <span class="date">2022</span>
                        <h2><a href="https://github.com/enyo-ojo/snake-game.github.io">Snake Game<br />
                                     app</a></h2>
                    </header>
                    <a href="#" class="image fit"><img src="images/image9.png" alt="" /></a>
                    <p>Snake Game Project  built with HTML,CSS and JS<br/> Click the title above to view code and below to view project</p>
                    <ul class="actions special">
                        <li><a href="https://enyo-ojo.github.io/snake-game.github.io/" class="button"> View Project</a></li>
                    </ul>
                </article>
                <article>
                    <header>
                        <span class="date">2022</span>
                        <h2><a href="https://github.com/enyo-ojo/accountSetup.github.io">Account Setup <br />
                                     Landing Page</a></h2>
                    </header>
                    <a href="#" class="image fit"><img src="images/img8.png" alt="" /></a>
                    <p>Account setup responsive design. <br/> Click the title above to view code and below to view project</p>
                    <ul class="actions special">
                        <li><a href="https://enyo-ojo.github.io/accountSetup.github.io/" class="button">View Project</a></li>
                    </ul>
                </article>
                <article>
                    <header>
                        <span class="date">2022</span>
                        <h2><a href="https://github.com/enyo-ojo/bbqpage.github.io">Barbeque Invite<br />
                                     landing page</a></h2>
                    </header>
                    <a href="#" class="image fit"><img src="images/img10.png" alt="" /></a>
                    <p>A landing page for a barbeque fest reservation. <br/> Click the title above to view code and below to view project</p>
                    <ul class="actions special">
                        <li><a href="https://enyo-ojo.github.io/bbqpage.github.io/" class="button"> view Project</a></li>
                    </ul>
                </article>
                <article>
                    <header>
                        <span class="date">2022</span>
                        <h2><a href="#">Business Card <br />
                                     design</a></h2>
                    </header>
                    <a href="#" class="image fit"><img src="images/image8.png" alt="" /></a>
                    <p>Business card design.</p>
                    <ul class="actions special">
                        <li><a href="#" class="button">Project</a></li>
                    </ul>
                </article>
                <article>
                    <header>
                        <span class="date">2022</span>
                        <h2><a href="https://github.com/enyo-ojo/teaplaces.github.io">Tea Place<br />
                                     landing page</a></h2>
                    </header>
                    <a href="#" class="image fit"><img src="images/img9.png" alt="" /></a>
                    <p>Tea place landing page to place orders<br/> Click the title above to view code and below to view project</p>
                    <ul class="actions special">
                        <li><a href="https://enyo-ojo.github.io/teaplaces.github.io/" class="button"> View Project</a></li>
                    </ul></article></section></div</body></html>
    ''', unsafe_allow_html=True)

     #top project
    st.write(f'''
    
    ''', unsafe_allow_html=True)
    

if __name__ == "__main__":
    homepage()

