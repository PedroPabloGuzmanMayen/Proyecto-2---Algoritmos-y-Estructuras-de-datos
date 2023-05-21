
import numpy as np
from neo4j import GraphDatabase

# Connect to the Neo4j database
driver = GraphDatabase.driver("neo4j+s://b0a9a659.databases.neo4j.io", auth=("neo4j", "n9_qBLezCVCaPJaivvf08qdDk47l4UGKaTx1x_d5QDk"))

# Define the query to retrieve the matrix and node names
query = """
MATCH (c:Career)-[r:HAS_TAG]->(f:Feature)
RETURN c.name AS career_name, f.name AS feature_name, r.Strong AS strong
"""

# Execute the query and retrieve the results
with driver.session() as session:
    result = session.run(query)

    # Initialize an empty matrix and arrays
    career_names = []
    feature_names = []
    matrix = np.empty((0, 0))

    # Iterate over the result and populate the matrix and arrays
    for record in result:
        career_name = record["career_name"]
        feature_name = record["feature_name"]
        strong = record["strong"]

        if career_name not in career_names:
            career_names.append(career_name)

        if feature_name not in feature_names:
            feature_names.append(feature_name)

        # Find the index of the career and feature in the arrays
        career_index = career_names.index(career_name)
        feature_index = feature_names.index(feature_name)

        # Expand the matrix size if needed
        if career_index >= matrix.shape[0]:
            matrix = np.pad(matrix, ((0, career_index - matrix.shape[0] + 1), (0, 0)), mode='constant')
        if feature_index >= matrix.shape[1]:
            matrix = np.pad(matrix, ((0, 0), (0, feature_index - matrix.shape[1] + 1)), mode='constant')

        # Assign the strong value to the corresponding position in the matrix
        matrix[career_index][feature_index] = strong

# Print the matrix, career names, and feature names
print("Matrix:")
print(matrix)

print("Career names:", career_names)
print("Feature names:", feature_names)

print()
print()
print(matrix[2,9])
