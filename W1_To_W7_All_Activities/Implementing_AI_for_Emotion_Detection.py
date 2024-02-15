input_str = input()
# TODO: Split the input into a list of strings and convert it to a new list of integers
intensity_list = list(map(int, input_str.split(',')))
# TODO: Define a function to analyze the predominant emotion based on the list of integers representing the intensity and a list of strings representing the emotions
def analyze_emotion(intensity_list):
    # TODO: Finding the index of the predominant emotion in the list of facial features
    
    emotions = ["Anger", "Happiness", "Sadness", "Surprise"]
    max_intensity_index = intensity_list.index(max(intensity_list))
        
    # TODO: Determining the predominant emotion based on the found index
    predominant_emotion = emotions[max_intensity_index]
        
    return predominant_emotion

# TODO: Print the predominant emotion
print(analyze_emotion(intensity_list))