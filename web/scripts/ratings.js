export function ratings(anime) {
    let newAnime = []
    for(let key in anime) {
        newAnime.push(anime[key])
    }

    newAnime.sort((a, b) => {

        if(a.peopleRated < 4 && b.peopleRated < 4) return 0
        if(a.peopleRated < 4) return 1
        if(b.peopleRated < 4) return -1
        return b.userRating/b.peopleRated - a.userRating/a.peopleRated

    })
    console.log(newAnime)

    let images = document.querySelector('.images')

    let imgHolder = document.createElement('div')
    imgHolder.classList.add('img-holder')
    images.append(imgHolder)

    for(let i = 0; i< 108; i++) {

        console.log(`${i+1}.`,newAnime[i].name, `${Math.floor(newAnime[i].userRating/newAnime[i].peopleRated *100)/100}`)

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

export function localRatings(anime) {
    let newAnime = []
    for(let key in anime) {
        newAnime.push(anime[key])
    }

    newAnime.sort((a, b) => {

        if(a.peopleRated < 2 && b.peopleRated < 2) return 0
        if(a.peopleRated < 2) return 1
        if(b.peopleRated < 2) return -1
        return (b.userRating/b.peopleRated - b.rating) - (a.userRating/a.peopleRated - a.rating)

    })
    console.log(newAnime)

    let images = document.querySelector('.images')

    let imgHolder = document.createElement('div')
    imgHolder.classList.add('img-holder')
    images.append(imgHolder)

    for(let i = 0; i< 63; i++) {

        console.log(`${i+1}.`,newAnime[i].name, "Our:", Math.floor(newAnime[i].userRating/newAnime[i].peopleRated *100)/100, "Avg:", newAnime[i].rating, "Diff:", Math.floor((newAnime[i].userRating/newAnime[i].peopleRated - newAnime[i].rating) *100)/100)

        if(i%9 == 0) {
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

export function localRatingsReversed(anime) {
    let newAnime = []
    for(let key in anime) {
        newAnime.push(anime[key])
    }

    newAnime.sort((a, b) => {

        if(a.peopleRated < 5 && b.peopleRated < 5) return 0
        if(a.peopleRated < 5) return 1
        if(b.peopleRated < 5) return -1
        return (a.userRating/a.peopleRated - a.rating) - (b.userRating/b.peopleRated - b.rating) 

    })
    console.log(newAnime)

    let images = document.querySelector('.images')

    let imgHolder = document.createElement('div')
    imgHolder.classList.add('img-holder')
    images.append(imgHolder)

    for(let i = 0; i< 108; i++) {

        console.log(`${i+1}.`,newAnime[i].name, "Our:", Math.floor(newAnime[i].userRating/newAnime[i].peopleRated *100)/100, "Avg:", newAnime[i].rating, "Diff:", Math.floor((newAnime[i].userRating/newAnime[i].peopleRated - newAnime[i].rating) *100)/100)

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

export function weightedRatings(anime) {
    let newAnime = []
    for(let key in anime) {
        newAnime.push(anime[key])
    }

    newAnime.sort((a, b) => {

        return b.userRating/((11-b.userRating/b.peopleRated)*(11-b.userRating/b.peopleRated)) - a.userRating/((11-a.userRating/a.peopleRated)*(11-a.userRating/a.peopleRated))

    })
    console.log(newAnime)

    let images = document.querySelector('.images')

    let imgHolder = document.createElement('div')
    imgHolder.classList.add('img-holder')
    images.append(imgHolder)

    for(let i = 0; i< 108; i++) {

        console.log(`${i+1}.`,newAnime[i].name, `${Math.floor(newAnime[i].userRating/((11-newAnime[i].userRating/newAnime[i].peopleRated)*(11-newAnime[i].userRating/newAnime[i].peopleRated)) *100)/100}`)

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

export function avgRatings(anime) {
    
    let overallTemp = 0, localTemp = 0
    let overallResult, localResult
    let i = 0
    for(let key in anime) {
        overallTemp += parseInt(anime[key].rating)
        localTemp += anime[key].userRating / anime[key].peopleRated
        i++
    }
    overallResult = Math.round(overallTemp/i*1000)/1000
    localResult = Math.round(localTemp/i*1000)/1000

    console.log(overallResult, localResult)
}