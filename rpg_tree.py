class StoryNode:
    """Represents a node in the decision tree."""
    def __init__(self, event_number, description, left=None, right=None):
        self.event_number = event_number
        self.description = description
        self.left = left
        self.right = right

class GameDecisionTree:
    """Binary decision tree for the RPG."""
    def __init__(self):
        self.nodes = {}  # Dictionary to store nodes
        self.root = None

    def insert(self, event_number, description, left_event, right_event):

        if event_number not in self.nodes:
            self.nodes[event_number] = StoryNode(event_number, description)

        node = self.nodes[event_number]
        node.description = description

        if left_event != -1:
            if left_event not in self.nodes:
                self.nodes[left_event] = StoryNode(left_event, "")
            node.left = self.nodes[left_event]

        if right_event != -1:
            if right_event not in self.nodes:
                self.nodes[right_event] = StoryNode(right_event, "")
            node.right = self.nodes[right_event]

        if self.root is None:
            self.root = node

    def play_game(self):
        current = self.root
        while current:
            print(f"\n{current.description}")
            if current.left is None and current.right is None:
                print("The story ends here. Thanks for playing!")
                break

            choice = input("Enter 1 or 2: ")
            if choice == "1" and current.left:
                current = current.left
            elif choice == "2" and current.right:
                current = current.right
            else:
                print("Invalid choice. Please enter 1 or 2.")

def load_story(filename, game_tree):
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(" | ")
            if len(parts) == 4:
                event_number = int(parts[0])
                description = parts[1]
                left_event = int(parts[2])
                right_event = int(parts[3])
                game_tree.insert(event_number, description, left_event, right_event)

# Main program
if __name__ == "__main__":
    game_tree = GameDecisionTree()
    load_story("story.txt", game_tree)
    game_tree.play_game()