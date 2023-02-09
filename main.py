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
             <svg class="bi bi-github" fill="currentColor" height="16" viewbox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg">
            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z">
            </path></svg>
             Project : <a class="text-dark" href="https://github.com/pj8912/wiki-blog-automation"> wiki-blog-automation </a>
            </span> <br />
          
               <span class="h5 text-dark"><svg class="bi bi-database-fill" fill="currentColor" height="16" viewbox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg">
            <path d="M3.904 1.777C4.978 1.289 6.427 1 8 1s3.022.289 4.096.777C13.125 2.245 14 2.993 14 4s-.875 1.755-1.904 2.223C11.022 6.711 9.573 7 8 7s-3.022-.289-4.096-.777C2.875 5.755 2 5.007 2 4s.875-1.755 1.904-2.223Z">
            <path d="M2 6.161V7c0 1.007.875 1.755 1.904 2.223C4.978 9.71 6.427 10 8 10s3.022-.289 4.096-.777C13.125 8.755 14 8.007 14 7v-.839c-.457.432-1.004.751-1.49.972C11.278 7.693 9.682 8 8 8s-3.278-.307-4.51-.867c-.486-.22-1.033-.54-1.49-.972Z">
            <path d="M2 9.161V10c0 1.007.875 1.755 1.904 2.223C4.978 12.711 6.427 13 8 13s3.022-.289 4.096-.777C13.125 11.755 14 11.007 14 10v-.839c-.457.432-1.004.751-1.49.972-1.232.56-2.828.867-4.51.867s-3.278-.307-4.51-.867c-.486-.22-1.033-.54-1.49-.972Z">
            <path d="M2 12.161V13c0 1.007.875 1.755 1.904 2.223C4.978 15.711 6.427 16 8 16s3.022-.289 4.096-.777C13.125 14.755 14 14.007 14 13v-.839c-.457.432-1.004.751-1.49.972-1.232.56-2.828.867-4.51.867s-3.278-.307-4.51-.867c-.486-.22-1.033-.54-1.49-.972Z">
              </path></path></path></path></svg> Source : <a class="text-dark" href="{url}">{title}</a>
             </span>
            </div>'''
        blogger.upload_blog.uploadblog(title, content)
