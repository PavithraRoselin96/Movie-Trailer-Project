import fresh_tomatoes
import media

#Creating instance for Ae_Dhil_He_Mushkil
Ae_Dil_Hai_Mushkil = media.Movie("Ae Dil Hai Mushkil",
                        "Ae Dil Hai Mushkil (English: This Heart is Complicated) is a 2016 Indian romantic drama film written and directed by Karan Johar. It features Aishwarya Rai Bachchan, Ranbir Kapoor and Anushka Sharma in lead roles. It was released on 28 October 2016 on the Diwali weekend.",
                        "https://upload.wikimedia.org/wikipedia/en/2/2a/Ae_Dil_Hai_Mushkil2.jpg",
                        "https://www.youtube.com/watch?v=Z_PODraXg4E")

#Creating instance for The_Chronicles_of_Narnia
The_Chronicles_of_Narnia = media.Movie("The Chronicles of Narnia",
                 "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe is a 2005 British-American high fantasy film directed by Andrew Adamson and based on The Lion, the Witch and the Wardrobe, the first published and second chronological novel in C. S. Lewis's children's epic fantasy series, The Chronicles of Narnia. William Moseley, Anna Popplewell, Skandar Keynes and Georgie Henley play Peter, Susan, Edmund, and Lucy, four British children evacuated during the Blitz to the countryside, who find a wardrobe that leads to the fantasy world of Narnia. There they ally with the Lion Aslan (voiced by Liam Neeson) against the forces of Jadis, the White Witch (Tilda Swinton).The film was released on December 9, 2005, in both Europe and North America to positive reviews and was highly successful at the box office grossing more than $745 million worldwide, making it 2005's third most successful film. It won the 2005 Academy Award for Best Makeup and various other awards.",
                 "https://upload.wikimedia.org/wikipedia/en/1/10/The_Chronicles_of_Narnia_-_The_Lion%2C_the_Witch_and_the_Wardrobe.jpg",
                 "https://www.youtube.com/watch?v=apoIn3lbmOM")

#Creating instance for Gravity
Gravity = media.Movie("Gravity",
                  "Gravity is a 2013 science fiction adventure film directed, co-written, co-edited and co-produced by Alfonso Cuarón. It stars Sandra Bullock and George Clooney as astronauts who are stranded in space after the mid-orbit destruction of their space shuttle, and their subsequent attempt to return to Earth.Gravity is a 2013 science fiction adventure film directed, co-written, co-edited and co-produced by Alfonso Cuarón. It stars Sandra Bullock and George Clooney as astronauts who are stranded in space after the mid-orbit destruction of their space shuttle, and their subsequent attempt to return to Earth.",
                  "https://upload.wikimedia.org/wikipedia/en/f/f6/Gravity_Poster.jpg",
                  "https://www.youtube.com/watch?v=OiTiKOy59o4")

#Creating instance for Jagga
Jagga = media.Movie("Jagga Jasoos",
                     "Jagga Jasoos is a Bollywood movie",
                     "https://upload.wikimedia.org/wikipedia/en/9/94/JaggaJasoosPoster.jpg",
                     "https://www.youtube.com/watch?v=YheC-4Qgoro")

#Creating instance for The Conjuring
Conjuring = media.Movie("The Conjuring",
                     "The Conjuring is a Thriller Movie about the exorcists Warren family.",
                     "https://upload.wikimedia.org/wikipedia/en/1/1f/Conjuring_poster.jpg",
                     "https://www.youtube.com/watch?v=k10ETZ41q5o")

#Creating instance for Premam
Premam= media.Movie("Premam",
                    "Premam (English: Wrestling competition) is a 2016 Indian Hindi-language biographical sports drama film directed by Nitesh Tiwari. ",
                    "https://upload.wikimedia.org/wikipedia/en/3/32/Premam_film_poster.jpg",
                    "https://www.youtube.com/watch?v=i6TSrhiuSJA")

#Putting those objects in a list
movies = [Ae_Dil_Hai_Mushkil, The_Chronicles_of_Narnia, Gravity, Jagga, Conjuring, Premam]

#Calling open_movies_page() function from fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
