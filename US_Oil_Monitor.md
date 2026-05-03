# U.S. Weekly WTI & Petroleum Monitor Project

## Tracking the Relationship Between U.S. Petroleum Supply, WTI Crude Oil Prices, and External Shocks

For our Advanced Computing project, our team built an interactive Streamlit web application to explore the relationship between weekly U.S. petroleum product supplied and WTI crude oil prices. The project was motivated by a simple but important question: how do energy market indicators move over time, and how might external shocks such as geopolitical conflicts affect oil prices and eventually consumer-facing gasoline prices? We wanted to create a tool that was not only analytical, but also easy for users to navigate and interpret.

The app integrates data from the U.S. Energy Information Administration (EIA), including weekly petroleum product supplied and WTI crude oil spot prices. We also incorporated external event context using GDELT to connect market movements with geopolitical and conflict-related events. The final app includes multiple pages: a main monitoring page for petroleum supply trends, a WTI-focused page for crude oil price movements, and an event context page that helps users understand how geopolitical shocks may transmit through oil markets.

## My Contribution

My main contribution focused on building and refining the Streamlit application, especially the user-facing structure and explanation of the analysis. I worked on organizing the app into clear pages, improving the sidebar navigation, adding explanatory text, and making sure the charts were understandable to users who may not have a technical background. I also contributed to the data pipeline logic, including connecting EIA API data and GDELT data to Big Query, aligning weekly time periods, and preparing the app for deployment through Streamlit Cloud. Through this process, I gained more experience working with APIs, cloud-based deployment, BigQuery, Python, and Streamlit.

One key challenge we faced was making the project both technically functional and narratively clear. Energy data can be difficult to interpret because supply, crude oil prices, gasoline prices, and geopolitical events are connected through multiple channels. To address this, we simplified the logic into a clear chain: geopolitical or conflict event → WTI crude oil price movement → potential impact on gasoline prices for U.S. consumers. This helped us frame our research questions more precisely: how much does conflict intensity in oil-producing countries affect WTI prices, how much does WTI affect U.S. gasoline prices, and how long does this transmission take? Also, the app run differently on local side and internet site. Since this is also a group project, we need to collaborate together and sometimes it is difficult to align our changes or commits immediately with the teaammate, making the project improvement slower. 

💙 But luckily we were able to solve all of them and build a super lovely website together! A big THANK YOU to my amazing teammate Indra!!

## What I Learned

This project helped me better understand how computational tools can be used to communicate complex policy and market issues. Beyond coding, I learned the importance of building data products that are interpretable, visually clear, and useful for decision-making. .This is my first app project and now I have so many ideas in the mind. In the future I want to build a personal website that contain all the recipes I recorded for bakery and cooking! This two-semester lecture let me gain coofidence in vibe coding! Really Appreciate everything!

## Project Links

- Live Streamlit App: [U.S. Weekly WTI & Petroleum Monitor](https://giggling-wombat-group-project.streamlit.app/)
- GitHub Repository: https://github.com/advanced-computing/giggling-wombat

## Sample Screenshots

### Homepage: Petroleum Supply Monitor

```{image} app.png
:alt: Homepage of the U.S. Oil Monitor app
:width: 800px
```

### Event Context and External Shocks Page

```{image} conflict contect.png
:alt: Event context page
:width: 800px
```