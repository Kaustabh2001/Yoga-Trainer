# Yoga-Trainer
> This repo is dedicated to my Yoga Posture Correction & Dumbbell-Curl Counter  modules, using OpenCV & MediaPipe for computing Human Pose Estimations, as parts of the project submission by Team Health_Hacktivists at DIRECTRIX'23, FIEM.

The "Yoga Posture Estimation and Correction System" is designed to facilitate accurate yoga practice by integrating advanced pose estimation techniques with real-time feedback. This innovative system employs a comprehensive approach to analyze yoga practitioners' postures and provide corrective guidance for optimal results.

## Features

- Real-time Pose Estimation: The system employs the MediaPipe pose estimation model to capture body key points during live yoga sessions.
- Posture Angle Analysis: Joint angles, including knees, hips, shoulders, and head, are calculated by referencing a database of images showcasing 18 different yoga poses.
- Personalized Feedback: A comparison between the user's current posture angles and the mean and standard deviation angles of each pose yields instant feedback on posture accuracy.
- Dynamic Correction Messages: The user receives real-time messages suggesting specific joint angle adjustments to refine their posture.
- Pygame UI

## Usage

1. Execute the main application.
2. Position the user in front of the camera to begin practicing the yoga pose.
3. The system provides real-time feedback, indicating whether the user's posture is aligned or requires correction.
4. Follow the dynamic correction messages to adjust joint angles and enhance posture accuracy.

## Description
### Pose Estimation
The preliminary generic pose estimation required for either of the activity categories is done by capturing the realtime footage from User's device cam using OpenCV.
The thus captured feed is then subjected to the posture estimation, using MediaPipe. These users' joint mapping coordinates are then used to do computations for the respective activity category applications.

### Yoga Pose
**Detection**: A set of 18 yoga poses is selected from the Yoga-82 Dataset, whose form can be adequately detected using only a single camera POV. These images are then subjected to pose estimation, after which we end up with an *average posture map* (the ratio in which the users' appendages and joints should be placed/distanced when doing that particular pose).
**Correction**: The users' live camera feed captured is subjected to pose estimation frame by frame and compared with Yoga Position's *average posture map*. The user is then nudged into the right posture through the alignment alerts suggesting fixes for the inconsistencies in posture.
**API**: This API serves to provide Yoga Correction Feedback in response to remote requests over the internet or through local system sockets.

### Curl Counter
A video feed of a professional instructor performing the exercise is captured and subjected to posture detection frame by frame. The angles formed by the joints of the concerned muscle group are calculated and the change in these angles is used to determine the apt threshold for counting a repetition/curl.
The users' live camera feed captured is subjected to pose estimation frame by frame and the angles formed between the joints of the concerned muscle group are calculated. Once the change in angle crosses the above threshold, a curl is counted.

### User Interface
**Pygame** is used to build a user interface for the user to choose between the Curl Counter & the Yoga Pose Correction modules, and the Yoga Pose the user will be doing when the latter is chosen.
The UI is designed to be used on small-screen devices such as those with a display width of ~15 inches.

## Prerequisites

- Python (>= 3.x)
- OpenCV
- MediaPipe

## Launch the main application:
run python Display_Window_main.py

The practitioner positions themselves in front of the integrated camera, selecting a yoga pose from the available 18 options.
The system provides immediate feedback on the alignment of their posture, evaluating joint angles against statistical data.
Practitioners receive constructive messages, suggesting adjustments for any imperfect joint angles, thereby refining their posture.
