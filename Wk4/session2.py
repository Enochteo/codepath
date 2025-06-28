# Problem

def count_unique_characters(script):
    return len(script)

script = {
    "Alice": ["Hello there!", "How are you?"],
    "Bob": ["Hi Alice!", "I'm good, thanks!"],
    "Charlie": ["What's up?"]
}
print(count_unique_characters(script)) 

script_with_redundant_keys = {
    "Alice": ["Hello there!"],
    "Alice": ["How are you?"],
    "Bob": ["Hi Alice!"]
}
print(count_unique_characters(script_with_redundant_keys)) 

def find_most_frequent_keywords(scenes):
    freq = {}
    for keywords in scenes.values():
        for word in keywords:
            #print(word)
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

    max_freq = max(freq.values())

    result = []

    for word, count in freq.items():
        if count == max_freq:
            result.append(word)
    
    result.sort()
    return result
        

scenes = {
    "Scene 1": ["action", "hero", "battle"],
    "Scene 2": ["hero", "action", "quest"],
    "Scene 3": ["battle", "strategy", "hero"],
    "Scene 4": ["action", "strategy"]
}
print(find_most_frequent_keywords(scenes))

scenes = {
    "Scene A": ["love", "drama"],
    "Scene B": ["drama", "love"],
    "Scene C": ["comedy", "love"],
    "Scene D": ["comedy", "drama"]
}
print(find_most_frequent_keywords(scenes))