export function popularity(anime) {
    let newAnime = []
    for(let key in anime) {
        newAnime.push(anime[key])
    }

    newAnime.sort((a, b) => b.peopleRated - a.peopleRated)
    console.log(newAnime)

    let images = document.querySelector('.images')

    let imgHolder = document.createElement('div')
    imgHolder.classList.add('img-holder')
    images.append(imgHolder)

    for(let i = 0; i< 108; i++) {

        console.log(`${i+1}.`,newAnime[i].name, `${Math.floor(newAnime[i].peopleRated/23 *100)}%`)

        if(i%12 == 0) {
            imgHolder = document.createElement('div')
            imgHolder.classList.add('img-holder')
            images.append(imgHolder)
        }

        if(newAnime[i].bigImage) {
            let img = document.createElement('img')
            img.classList.add('image')
            img.src = newAnime[i].bigImage
            imgHolder.append(img)
        }
    }
}

export function localPopularity(anime) {
    let newAnime = []
    for(let key in anime) {
        newAnime.push(anime[key])
    }

    newAnime.sort((a, b) => {
        if(a.peopleRated <= 2 && b.peopleRated <= 2) return 0
        else return b.peopleRated/b.members - a.peopleRated/a.members
    })
    console.log(newAnime)

    let images = document.querySelector('.images')

    let imgHolder = document.createElement('div')
    imgHolder.classList.add('img-holder')
    images.append(imgHolder)

    for(let i = 0; i< 108; i++) {

        console.log(`${i+1}.`,newAnime[i].name, `${Math.floor(newAnime[i].peopleRated/23 *100)}%`)

        if(i%12 == 0) {
            imgHolder = document.createElement('div')
            imgHolder.classList.add('img-holder')
            images.append(imgHolder)
        }

        
        if(newAnime[i].bigImage) {
            let img = document.createElement('img')
            img.classList.add('image')
            img.src = newAnime[i].bigImage
            imgHolder.append(img)
        }
        else {
            let txt = document.createElement('div')
            txt.classList.add('text-container')
            let p = document.createElement('p')
            p.classList.add('title')
            p.innerHTML = newAnime[i].name
            txt.append(p)
            imgHolder.append(txt)
        }
    }
}