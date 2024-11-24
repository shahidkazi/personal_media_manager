# Personal Media Manager
Python based Movie and TV Series collection manager

Tired of trying to find a media manager for your DVDs, Blu-Rays and Downloads?
I was... The ones I found we either too expensive or had too much than one can manage.

So I decided to build one, open source, so anyone can use and extend as needed (with due credit ofcourse).<br/><br/>
So enjoy collecting and managing your Movies and TV Series...<br/><br/>
<b><u>Current Feautures:</u></b>
<ul>
    <li>
        Add Movies and Tv Series from Media -> Add New menu or the '+' icon on the toolbar<br/><br/>
        <img src="images/screens/001-movies.png" width="500" /><br/><br/>
        <img src="images/screens/004-series.png" width="500" /><br/>
    </li>
    <li>Add custom Genres and Languages from the General Tab<br/></li>
    <li>Add/Remove Poster from the General Tab<br/></li>
    <li>
        Update any properties in the General, Media, Episodes tabs and use Update Media to Save<br/><br/>
        <img src="images/screens/002-movie-media.png" width="500" /><br/><br/>
        <img src="images/screens/003-movie-cast.png" width="500" /><br/>
    </li>
    <li>Use Media -> Delete or the Delete Icon on the Toolbar to delete movies / series (multi-select supported)<br/></li>
    <li>
        Use Media -> Bulk Update to update common properties for multiple selected movies (not supported for series)<br/><br/>
        <img src="images/screens/010-bulk-update.png" width="500" /><br/>
    </li>
    <li>
        Use Media -> Fetch Details or the IMDB icon to get details of the movie/series from IMDB (multi-select supported)<br/><br/>
        <img src="images/screens/009-imdb.png" width="500" /><br/>
    </li>
    <li>You can build custom scrapers and add to the templates directory following implementing the required methods and making an entry in registry.json<br/></li>
    <li>
        Use Media -> Import / Export to import and export from and to popular formats like CSV/XLSX/JSON<br/><br/>
        <img src="images/screens/011-import.png" width="500" /><br/><br/>
        <img src="images/screens/012-export.png" width="500" /><br/>
    </li>
    <li>You can build custom importers and exporters like above<br/></li>
    <li>Publish is similar to export but with additional functionality. Have added a sample publisher for Firebase. You can build ones for creating web sites or publishing to other online sources<br/></li>
    <li>
        The Episodes Tab (only visible for series) you can view / add / delete episodes (multi-select supported except for edit)<br/><br/>
        <img src="images/screens/005-series-episodes.png" width="500" /><br/>
    </li>
    <li>The Media Tab lets you set media details for Movies and in case you have added a disc tag for the media shows you which other media has the same tag (on the same disc)<br/></li>
</ul>
Please do reach out to me at <a href="mailto:shahidskazi@hotmail.com">shahidskazi@hotmail.com</a> or leave message on GitHub and I shall try my best to get back to you.