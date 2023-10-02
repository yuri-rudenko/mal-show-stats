export function favCharacters(users) {

    function fetchJSONData(filePath, callback) {
        fetch(filePath)
            .then(response => response.json())
            .then(data => callback(data))
            .catch(error => console.error('Error fetching JSON:', error));
    }

    fetchJSONData('../../../../myAnimeCharacters.json', function(characters) {

        let chars = new Map()
        let anime = new Map()

        for(let key in users) {
            for(let char of users[key].favCharacters) {
                
                if(chars[char.name]) {
                    chars[char.name] += 1
                }
                else {
                    chars[char.name] = 1
                }
                if(anime[char.anime]) {
                    anime[char.anime] += 1
                }
                else {
                    anime[char.anime] = 1
                }
            }
        }

        let charsArr = []
        let animeArr = []

        for(let key in chars) {
            charsArr.push({
                name: key,
                popularity: chars[key]
            })
        }
        for(let key in anime) {
            animeArr.push({
                name: key,
                popularity: anime[key]
            })
        }

        charsArr.sort((a,b) => b.popularity - a.popularity)
        animeArr.sort((a,b) => b.popularity - a.popularity)
        console.log(animeArr)

        let images = document.querySelector('.images')
        let imgHolder = document.createElement('div')
    
        for(let i = 0; i< 25; i++) {
    
            if(i%5 == 0) {
                imgHolder = document.createElement('div')
                imgHolder.classList.add('img-holder')
                images.append(imgHolder)
            }

            for(let char of characters) {
                
                if(charsArr[i].name == char.Name) {
                    charsArr[i].link = char.Link
                    break;
                }
            }

            let rating = document.createElement('p')
            rating.classList.add('char-popularity')
            rating.innerHTML = charsArr[i].popularity
            let imgWrapper = document.createElement('div')
            imgWrapper.classList.add('image-wrapper')
            let img = document.createElement('img')
            img.src = charsArr[i].link
            img.classList.add('image')
            imgWrapper.append(img)
            imgWrapper.append(rating)
            imgHolder.append(imgWrapper)
        }

    })
}

export function favAnime(users, animeData) {

    let anime = new Map()

    for(let key in users) {

        for(let title of users[key].favAnime) {
            
            if(anime[title]) {
                anime[title] += 1
            }
            else {
                anime[title] = 1
            }
        }
    }

    let animeArr = []

    for(let key in anime) {
        animeArr.push({
            name: key,
            popularity: anime[key]
        })
    }

    animeArr.sort((a,b) => b.popularity - a.popularity)
    console.log(animeArr)

    let images = document.querySelector('.images')
    let imgHolder = document.createElement('div')
    
    for(let i = 0; i< 33; i++) {
    
        if(i%6 == 0) {
            imgHolder = document.createElement('div')
            imgHolder.classList.add('img-holder')
            images.append(imgHolder)
        }

        let rating = document.createElement('p')
        rating.classList.add('char-popularity')
        rating.innerHTML = animeArr[i].popularity
        let imgWrapper = document.createElement('div')
        imgWrapper.classList.add('image-wrapper')
        let img = document.createElement('img')
        console.log(animeData[animeArr[i].name])
        img.src = animeData[animeArr[i].name].bigImage
        img.classList.add('image')
        imgWrapper.append(img)
        imgWrapper.append(rating)
        imgHolder.append(imgWrapper)
    }
}
