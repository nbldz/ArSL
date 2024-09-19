from Code.modules import *
#from Code.landmark_detection import results
import torch
import torch.nn as nn
import torch.optim as optim


def extract_keypoints(results):
    pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(25)
    face = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark]).flatten() if results.face_landmarks else np.zeros(50)
    left_hand = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(30)
    right_hand = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(30)
    
    # # Define a simple neural network for fusion
    # class FusionNet(nn.Module):
    #     def __init__(self, input_size, hidden_size, output_size):
    #         super(FusionNet, self).__init__()
    #         self.fc1 = nn.Linear(input_size, hidden_size)
    #         self.fc2 = nn.Linear(hidden_size, output_size)
        
    #     def forward(self, x):
    #         x = torch.relu(self.fc1(x))
    #         x = self.fc2(x)
    #         return x
    
    # # Initialize the fusion model
    # input_size = len(fused_vector)
    # hidden_size = 64
    # output_size = 1  # Output size can be adjusted based on the task
    # fusion_model = FusionNet(input_size, hidden_size, output_size)
    
    # # Convert fused vector to PyTorch tensor
    # fused_vector_tensor = torch.FloatTensor(fused_vector)
    
    # # Forward pass through the fusion model
    # output = fusion_model(fused_vector_tensor)
    return np.concatenate([ left_hand, right_hand,pose,face])