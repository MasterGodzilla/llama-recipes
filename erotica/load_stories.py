import os

while True:
    # Get the title from the user
    title = input("Please enter the title (or 'exit' to quit): ")
    
    # Exit condition
    if title.lower() == 'exit':
        break

    # Get the other details from the user
    plot = input("Please enter the plot: ")
    tags = input("Please enter the tags: ")
    
    
    print("Please enter the main story (type 'END' on a new line to finish): ")
    lines = []
    while True:
        line = input()
        if line == 'END':
            break
        lines.append(line)
    
    # Combine the story lines into a single string
    main_story = '\n'.join(lines)
    
    # Create the output string
    output = f"Title: {title}\n\nTags: {tags}\n\nPlot: {plot}\n\nMain Story: {main_story}"
    
    # Get a safe filename
    filename = "".join([c for c in title if c.isalpha() or c.isdigit() or c==' ']).rstrip()
    filename = filename.replace(" ", "_")
    
    # Save the output to a file
    with open(f"{filename}.txt", "w") as f:
        f.write(output)
    
    print(f"The story has been saved to {filename}.txt")
