# ClothingScraper
  The primary goal of this script is to create a tool with which buyers are better able to retrieve specific objects which they are looking for, and among them, find the best price. In the reselling community, the term ISO refers to 'In Search Of', typically used when a buyer is looking for something specific e.g. "ISO LoveShackFancy Kassius Cardigan". This usually invites members of the reselling community to share the object in the hopes it'll eventually reach a seller, though this process is lengthy and inefficient, on top of that, searching through troves of clothing is a tiring and time-consuming task; however, we are hoping to automate this approach by building a tool that will a) scrape these websites using a given name, description, or image that the user gives, with attributes like material, size, color, and brand being taken into consideration. 
  Then b) if the name of some desired item is unknown and unavailable by seller and/or buyer, this tool will aim to scrape these websites and retrieve the unnamed, non-descript images and return those posts as well, this second part will utilize computer vision models which will be trained to identify objects of the same design in various backgrounds, poses, etc. This tool will target clothing reselling sites specifically. 

## General Considerations
* Size
  * Numeric for tops
  * Numeric for bottoms (24", 25", etc.)
  * International sizing (36FR VS 36IT)
  * Shoe sizing
  * Letter for tops and bottoms (XS, S, M, L) 
* Budget
* Name
  * Optional paramter 
* Brand
* Color
* Material
  * Synthetic
  * Natural
  * Semi-synthetic 
* Images (image pathway)
* Category
  * Accessories
  * Clothing
    * Tops
      * Blouses
      * Camisoles
      * Zip-ups
      * Etc.
    * Bottoms
      * Shorts
      * Skirts
      * Jeans
      * Etc.
    * Jackets
      * Coats
      * Knits
      * Denim
      * Etc.
    * Dresses
      * Mini
      * Midi
      * Maxi
      * Etc.
  * Shoes
      * Boots
        * Ankle boots
        * Knee-high boots 
      * Sneakers
        * Casual sneakers
        * Athletic sneakers
      * Etc.     
* Condition
  * New With Tags
  * New Without Tags
  * Excellent Used Condition
  * Good Used Condition
  * Slightly Flawed/Damaged
  * Very Flawed/Damaged
  * Etc.    

## Webscraping Aspect

Features:
* Scrapes through reselling websites like Depop, Mercari, eBay, and Poshmark (there exist more, but for now we are limiting it to these, as they are among the most popular reselling platforms)
* Should accept inputs that make up the description of what the user is looking for; should be able to accept blank inputs as well e.g. N/A if the user has no size preference, has no color preference, but it should minimally contain a few parameters: budget, brand, and category
* It should return all the links of the posts it's collected that match the description of the clothing piece(s) that the user is looking for, and point out which among them has the best (lowest) price, perhaps through an email

## ML/Comp Vision Aspect
  If a user is looking for something in which they are missing a name or brand, or perhaps they are looking for a specific piece of clothing made by company which doesn't 'name' their products (e.g. Zara will only ever have "lace ruffle camisole" instead of naming the object like a another brand might, e.g. Reformation will have a "Wyn" or "Renna" top which is rarely shared by other clothing pieces produced by the brand, at least in the same category, making searching for a particular item easy. 
  However, even in the case that the brand gives names to their clothing pieces, sometimes, users will have forgotten or not know or not add this name to their product description so, if, say, we are searching for the Free People Lottie dress, though searching for it on resale sites will yield many results, there are many more Lottie dresses out there that are not found by searching up the name, because they'll go under a different description instead, i.e. "Free People white long sleeve mini dress", meaning that solely searching for the name will not actually yield the optimal price.
  Therefore, we will try to use computer vision to make up for the troves and troves of descriptionless pieces of clothing that people are actually searching for and desire. As humans, we are able to identify a piece of clothing quite well, and, if you have grown accustomed to the fabrics, prints, etc. used by a brand, you will be able to attribute the look of a clothing to perhaps a certain brand and even era of the brand. We hope to create a computer vision model that can hone in on the essence of particular brands and styles, so that it will be able to identify pieces of clothing as well as a human can and account for the masses of clothing being dumped onto the internet that don't receive a second glance despite being what people are looking for.
  Like the webscraper, it should return all the links of the posts it's collected that match the description of the clothing piece(s) that the user is looking for, and point out which among them has the best (lowest) price, perhaps through an email.

