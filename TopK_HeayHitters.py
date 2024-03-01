# The Top-K Heavy Hitters problem is a common scenario in data processing
# where we want to find the most frequent items (heavy hitters) in a data stream. 
# The "Fast" and "Slow" approaches refer to different methodologies for calculating these heavy hitters, 
# each with its own trade-offs. Here’s an outline for both:

# Fast Approach (Approximation)
# Message Queue (e.g., Kafka): Stream of events or data points are sent to a message queue 
# to be processed asynchronously. Kafka is often used for its high throughput and scalability.

# Count-Min Sketch: An efficient probabilistic data structure that uses 
# hash functions to count occurrences of events with a controlled error margin. 
# It’s great for streams with a high volume of data and where an approximation is acceptable.

# In-Memory Data Store (e.g., Redis): 
# The Count-Min Sketch data is stored in an in-memory data store for fast reads and writes.

# Approximate Top-K Calculation: Using the data from the Count-Min Sketch, 
# we can quickly calculate an approximate list of Top-K items. 
# This may not be completely accurate but gives a near real-time view.

# Update Leaderboard: The leaderboard is updated with the approximate Top-K items, 
# allowing for quick user feedback.

# Slow Approach (Exact Counts)
# Message Queue (e.g., Kafka): As with the fast approach, the stream starts at the message queue.

# Streaming Data Processor (e.g., Apache Spark Streaming, Flink): 
# A more sophisticated streaming data processor takes in the data stream and computes exact counts. 
# This is slower because it requires stateful computation.

# Persistent Data Store (e.g., PostgreSQL, NoSQL database): 
# The exact counts are stored in a persistent data store which allows for complex queries 
# but with higher read/write latency compared to in-memory stores.

# Exact Top-K Calculation: 
# A more accurate Top-K list is calculated from the exact counts. 
# This process is slower due to the additional overhead of exact computation and storage latency.

# Update Leaderboard: The leaderboard is updated less frequently but with exact data, ensuring accuracy.

# When to Use Each Approach
# Fast Approach: When near-real-time feedback is essential and slight inaccuracies are acceptable. 
# This is common in scenarios where the volume of data is massive and fast response times are critical, 
# such as monitoring dashboards or live recommendations.

# Slow Approach: When accuracy is crucial and the system can tolerate some delays in updates. 
# This is important in scenarios where decisions are made based on the Top-K results, 
# such as financial analysis or inventory restocking based on sales data.

# Alternative Approaches
# Hybrid Approach: Some systems use a combination of both methods, 
# using the fast approach for initial estimation 
# and the slow approach to periodically correct and update the leaderboard.

# Sampling and Micro-Batching: In some scenarios, 
# systems sample the data or process it in micro-batches to strike a balance between speed and accuracy.

# In both approaches, a crucial aspect is the ability to scale horizontally 
# as the volume of data increases. The choice of approach depends on specific application needs, 
# such as latency requirements, data volume, and accuracy.


# Adjust the nodes to reflect the shared message queue and client input
from matplotlib import pyplot as plt


nodes_shared = {
    'Client': (-1, 1),
    'Message Queue\n(Kafka)': (1, 1),
    'Count-Min Sketch\n(Fast Approximation)': (3, 2),
    'In-Memory Data Store\n(e.g., Redis)': (5, 2),
    'Approximate Top-K\nCalculation': (7, 2),
    'Update Leaderboard\n(Fast)': (9, 2),
    'Streaming Data Processor\n(e.g., Spark/Flink)': (3, 0),
    'Persistent Data Store\n(e.g., DB)': (5, 0),
    'Exact Top-K\nCalculation': (7, 0),
    'Update Leaderboard\n(Slow)': (9, 0)
}

# Adjust the edges to reflect the shared message queue and client input
edges_shared = [
    ('Client', 'Message Queue\n(Kafka)'),
    ('Message Queue\n(Kafka)', 'Count-Min Sketch\n(Fast Approximation)'),
    ('Message Queue\n(Kafka)', 'Streaming Data Processor\n(e.g., Spark/Flink)'),
    ('Count-Min Sketch\n(Fast Approximation)', 'In-Memory Data Store\n(e.g., Redis)'),
    ('In-Memory Data Store\n(e.g., Redis)', 'Approximate Top-K\nCalculation'),
    ('Approximate Top-K\nCalculation', 'Update Leaderboard\n(Fast)'),
    ('Streaming Data Processor\n(e.g., Spark/Flink)', 'Persistent Data Store\n(e.g., DB)'),
    ('Persistent Data Store\n(e.g., DB)', 'Exact Top-K\nCalculation'),
    ('Exact Top-K\nCalculation', 'Update Leaderboard\n(Slow)')
]

# Create the plot for the diagram with shared elements
plt.figure(figsize=(12, 7))

# Draw the nodes
for node, (x, y) in nodes_shared.items():
    plt.scatter(x, y, s=3000, color='lightgreen' if 'Fast' in node else 'lightcoral')
    plt.text(x, y, node, ha='center', va='center', weight='bold', fontsize=9)

# Draw the edges
for start, end in edges_shared:
    start_x, start_y = nodes_shared[start]
    end_x, end_y = nodes_shared[end]
    arrowprops=dict(arrowstyle="->", color="black", lw=2)
    plt.annotate('', xy=(end_x, end_y), xytext=(start_x, start_y), arrowprops=arrowprops)

# Remove axes and display the diagram
plt.axis('off')
plt.tight_layout()
plt.show()
