import pygame
import speech_recognition as sr
from gtts import gTTS
import os
import time

# Initialize pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Talking Tom Cat")

# Load cat image (replace with a valid path to an image of a cat)
cat_image = pygame.image.load('Tom.jpg')  # Ensure you have a cat image

# Load font
font = pygame.font.Font(None, 36)

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        # Convert speech to text
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand that.")
        return None
    except sr.RequestError:
        print("Sorry, the service is down.")
        return None

# Function to make the cat repeat the text
def speak_text(text):
    if text:
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        os.system("start output.mp3")  # For Windows, use 'start', for Mac use 'afplay', for Linux use 'mpg321'
        time.sleep(2)  # Wait for the speech to finish

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw the cat image
    screen.fill((255, 255, 255))  # Fill screen with white
    screen.blit(cat_image, (150, 100))  # Draw the cat image at the desired location

    # Display instructions
    text = font.render("Click to talk to the cat!", True, (0, 0, 0))
    screen.blit(text, (180, 20))
    
    pygame.display.flip()

    # Detect mouse click to start speaking
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:  # Left mouse button is clicked
        user_input = recognize_speech()
        if user_input:
            speak_text(user_input)
    
    pygame.time.wait(100)

pygame.quit()
