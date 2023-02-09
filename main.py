import imdblist as imdb
import getwiki as wiki 
import threading
import blogger 


lists = imdb.getlist.get_movie_list()
movie_title = [e for e in lists]
# print(movie_title)


movie_s = movie_title[2:]



for title in movie_s:
    check_result = wiki.check_cat.check_category(title)
    if check_result == 1:
        url = wiki.create_url.createurl(title)
        plot = wiki.getplots.Plot(url)
        imageurl = wiki.image_url.WikiImage(url)
        plot.start()
        imageurl.start()
        plot.join()
        imageurl.join()
        if imageurl.image_url == None:
            imageurl.image_url = "https://davidkoepp.com/wp-content/themes/blankslate/images/Movie%20Placeholder.jpg"
        
        if plot.plot == None:
            plot.plot = "No plot available for this movie"

        content = f'''<link crossorigin="anonymous" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" rel="stylesheet"></link>
        <h1 class="text-center text-dark">{title}</h1><br>
        <div class='text-center'> <img align='center' class='img-fluid'  src='{imageurl.image_url}' style='display: block; margin-left: auto; margin-right: auto; width: 300px;'></div>
        
        <div class="card card-body border-0 text-dark" style="font-family: arial; font-size: 20px; margin-top: 100px; padding: 20px;">{plot.plot}</div><hr>
        
        <div class="card card-body m-auto mt-5 text-dark bg-light">
             <span class="h5">
             <svg class="bi bi-github" fill="currentColor" height="18" viewbox="0 0 16 16" width="18" xmlns="http://www.w3.org/2000/svg">
            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z">
            </path></svg>
             Project : <a class="text-dark" href="https://github.com/pj8912/wiki-blog-automation"> wiki-blog-automation </a>
            </span> <br />
          
               <span class="h5 text-dark"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="bi bi-database" viewBox="0 0 16 16">
  <path d="M4.318 2.687C5.234 2.271 6.536 2 8 2s2.766.27 3.682.687C12.644 3.125 13 3.627 13 4c0 .374-.356.875-1.318 1.313C10.766 5.729 9.464 6 8 6s-2.766-.27-3.682-.687C3.356 4.875 3 4.373 3 4c0-.374.356-.875 1.318-1.313ZM13 5.698V7c0 .374-.356.875-1.318 1.313C10.766 8.729 9.464 9 8 9s-2.766-.27-3.682-.687C3.356 7.875 3 7.373 3 7V5.698c.271.202.58.378.904.525C4.978 6.711 6.427 7 8 7s3.022-.289 4.096-.777A4.92 4.92 0 0 0 13 5.698ZM14 4c0-1.007-.875-1.755-1.904-2.223C11.022 1.289 9.573 1 8 1s-3.022.289-4.096.777C2.875 2.245 2 2.993 2 4v9c0 1.007.875 1.755 1.904 2.223C4.978 15.71 6.427 16 8 16s3.022-.289 4.096-.777C13.125 14.755 14 14.007 14 13V4Zm-1 4.698V10c0 .374-.356.875-1.318 1.313C10.766 11.729 9.464 12 8 12s-2.766-.27-3.682-.687C3.356 10.875 3 10.373 3 10V8.698c.271.202.58.378.904.525C4.978 9.71 6.427 10 8 10s3.022-.289 4.096-.777A4.92 4.92 0 0 0 13 8.698Zm0 3V13c0 .374-.356.875-1.318 1.313C10.766 14.729 9.464 15 8 15s-2.766-.27-3.682-.687C3.356 13.875 3 13.373 3 13v-1.302c.271.202.58.378.904.525C4.978 12.71 6.427 13 8 13s3.022-.289 4.096-.777c.324-.147.633-.323.904-.525Z"/>
</svg>
            </div>'''
        blogger.upload_blog.uploadblog(title, content)


