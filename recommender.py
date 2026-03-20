def recommend_tool(collection, genre, difficulty, platform=None):

    difficulty_map = {
        "Beginner": 1,
        "Intermediate": 2,
        "Advanced": 3
    }

    user_level = difficulty_map[difficulty]

    # Step 1: Exact match
    exact = list(collection.find({
        "genre": genre,
        "difficulty": difficulty
    }))

    if exact:
        return exact[0]

    # Step 2: fallback to same genre
    tools = list(collection.find({"genre": genre}))

    if not tools:
        return {"error": "No tools found for this genre"}

    # Step 3: find closest difficulty
    best_tool = None
    min_diff = float("inf")

    for tool in tools:
        tool_level = difficulty_map[tool["difficulty"]]
        diff = abs(tool_level - user_level)

        if diff < min_diff:
            min_diff = diff
            best_tool = tool

    return best_tool