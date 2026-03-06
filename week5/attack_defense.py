# Cybersecurity Attack–Defense Simulation using Minimax

def minimax(depth, is_defender):

    # Base condition
    if depth == 0:
        print("Reached leaf node → Security score = 0")
        return 0

    # Defender's turn (maximize security)
    if is_defender:
        print("\nDefender's Turn (Depth:", depth, ")")
        best_score = float('-inf')

        actions = ["Apply Firewall", "Activate Intrusion Detection"]

        for action in actions:
            print("Defender action:", action)
            score = minimax(depth - 1, False)
            best_score = max(best_score, score)

        return best_score

    # Attacker's turn (minimize security)
    else:
        print("\nAttacker's Turn (Depth:", depth, ")")
        best_score = float('inf')

        actions = ["Launch Malware Attack", "Perform Phishing Attack"]

        for action in actions:
            print("Attacker action:", action)
            score = minimax(depth - 1, True)
            best_score = min(best_score, score)

        return best_score


# Run the simulation
depth = 3
result = minimax(depth, True)

print("\nFinal Optimal Security Outcome Score:", result)