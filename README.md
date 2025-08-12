# 🧠 BlinkSense: AI Powered Eye Blinking System  

This project is an AI-based real-time eye blink detection system that enables individuals with motor disabilities to interact with computers using left/right blinks. Built with computer vision, it uses a webcam feed to detect blink patterns and trigger specific actions, such as generating random letters for communication.  

### ⚙️ Components  
- **User Interface**: Accessible and user-friendly web interface for interaction.  
- **Blink Detection Module**: Detects and differentiates between left and right eye blinks.  
- **Action Trigger Module**: Executes corresponding actions based on detected blink type.  
- **Real-time Video Processing**: Processes webcam feed in real time for instant feedback.  

## 🛠️ Technologies Used  
- Python 3.x  
- MediaPipe  
- OpenCV  
- Flask  
- HTML, CSS, JavaScript  

## 🧠 Workflow (CV Pipeline)  

```text
Start → Capture Webcam Feed → Detect Facial Landmarks → Identify Blink Events
   → Classify Left/Right Blink → Trigger Action → Display Feedback → End
