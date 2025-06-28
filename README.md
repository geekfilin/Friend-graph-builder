Social graph visualiser v1.7(first uploaded source)
by filin

Description  
This tool collects data about social connections of users from Twitter and VK, builds an interaction graph, and identifies communities. The obtained data can be visualized and analyzed in graph processing software.  

 How It Works  
1. The script retrieves a list of followers and friends of the target user via social network APIs  
2. Filters weak connections based on a specified interaction threshold  
3. Builds a graph where nodes represent users and edges represent their interactions  
4. Applies a clustering algorithm to detect communities  
5. Saves results in GEXF format for further analysis  

Requirements  
- Python 3.8 or newer  
- API keys from Twitter and VK (instructions below)  

Installation  
1. Clone the repository:  
git clone https://github.com/yourusername/social-graph-visualizer.git
cd social-graph-visualizer
  

2. Install dependencies:  
pip install -r requirements.txt
 

API Setup  
Before using, you need to obtain and add API keys:  

For Twitter:
1. Register at developer.twitter.com  
2. Create an application  
3. Get the keys: consumer_key, consumer_secret, access_token, access_token_secret  

For VK: 
1. Create a Standalone application at vk.com/dev  
2. Obtain a Service Token  

Add the keys to the config.yaml file  

Usage  
Run the script:  
python main.py


Enter the requested data:  
- Username or ID  
- Platform (twitter or vk)  

Results will be saved in the outputs folder:  
- Graph in GEXF format (can be opened in Gephi)  
- Visualization image (optional)  

Sample Output  
The graph will contain:  
- Central node - the target user  
- First-level nodes - their followers/friends  
- Node colors - different communities  

Limitations  
1. Twitter API has a limit of 900 requests per 15 minutes  
2. VK requires an application token  
3. Instagram and Facebook are not currently supported  
