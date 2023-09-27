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
    const coeficient = 22/3807661
    let newAnime = []
    for(let key in anime) {
        newAnime.push(anime[key])
    }

    newAnime.sort((a, b) => {
        if(a.peopleRated < 3 && b.peopleRated < 3) return 0
        if(a.peopleRated < 3) return 1
        if(b.peopleRated < 3) return -1
        else return b.peopleRated/b.members - a.peopleRated/a.members
    })
    console.log(newAnime)

    let images = document.querySelector('.images')

    let imgHolder = document.createElement('div')
    imgHolder.classList.add('img-holder')
    images.append(imgHolder)

    for(let i = 0; i< 80; i++) {

        let compare = (Math.round(newAnime[i].peopleRated/newAnime[i].members*1000000)/1000000)/(Math.round(coeficient*1000000)/1000000)
        console.log(`${i+1}.`,newAnime[i].name, `${Math.round(compare*100)/100}`)

        if(i%10 == 0) {
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

export function lowestPopularity(anime) {
    let newAnime = []
    for(let key in anime) {
        newAnime.push(anime[key])
    }

    newAnime.sort((a, b) => parseInt(a.popularity)- parseInt(b.popularity)) 
    console.log(newAnime)

    let unpopular = []
    let i = 0
    while(unpopular.length < 10) {
        if(parseInt(newAnime[i].popularity) != parseInt(newAnime[i+1].popularity) - 1) {
            unpopular.push(i+2)
        }
        i++
    }
    console.log(unpopular)

}