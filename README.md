# Geography-Game
A Small game, where you have guess every country or state on a map (main.py) <br />
The datacreator.py allows you to easily add new maps <br />
Missed states or countrys will be listet in the output folder <br />
----------

How to play the game: <br />
  Run main.py. <br />
  Chose a map, and guess countries. <br />
  When you are finshed the programm will generate a file that you can find in the ./output folder, where is lists every country that you have failed to guess. <br />
  
----------

How to use the data creator in datacreator.py<br />
  If you want to add additional countries/states or create a new data set (=Map) from scratch, set the map_name to name of the map you want to create/edit.<br />
  Hint: it has to have a background image already saved with this exact name, previously saved data is optional.<br />
<br />
To add new countries click on the center of your chosen country and enter the name of it in the field that pops up <br />
If you are finished with your map click the red cross on the top right corner of the window <br />
Now you should be able to select the map, when you run main.py <br />
<br />
  e.g.:
  to create a map called „africa“ you have to have already safed a background image in the ./maps folder. This image hast o be a .gif file. If you just want to visualise every country se tappend to False, to edit the data set, keep append as True.
