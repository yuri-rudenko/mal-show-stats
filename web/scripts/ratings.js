export function ratings(anime) {
    let newAnime = []
    for(let key in anime) {
        if(anime[key].name.includes('')) {
            newAnime.push(anime[key])
        }
    }

    newAnime.sort((a, b) => {

        if(a.peopleRated < 4 && b.peopleRated < 4) return 0
        if(a.peopleRated < 4) return 1
        if(b.peopleRated < 4) return -1
        return (b.userRating/b.peopleRated - a.userRating/a.peopleRated)

    })
    console.log(newAnime)

    let images = document.querySelector('.images')

    let imgHolder = document.createElement('div')
    imgHolder.classList.add('img-holder')
    images.append(imgHolder)


    for(let i = 0; i< 48; i++) {

        let imgWrapper = document.createElement('div')
        imgWrapper.classList.add('image-wrapper')

        let rating = document.createElement('p')
        rating.classList.add('rating')
        rating.innerHTML = Math.floor(newAnime[i].userRating/newAnime[i].peopleRated *100)/100

        let position = document.createElement('p')
        position.classList.add('position')
        position.innerHTML = i+1

        console.log(`${i+1}.`,newAnime[i].name, `${rating.innerHTML}`)

        if(i%8 == 0) {
            imgHolder = document.createElement('div')
            imgHolder.classList.add('img-holder')
            images.append(imgHolder)
        }

        if(newAnime[i].bigImage) {
            let img = document.createElement('img')
            img.classList.add('image')
            img.src = newAnime[i].bigImage
            imgWrapper.append(img)
            imgWrapper.append(position)
            imgWrapper.append(rating)
            imgHolder.append(imgWrapper)
        }
        else {
            let txt = document.createElement('div')
            txt.classList.add('text-container')
            let p = document.createElement('p')
            p.classList.add('title')
            p.innerHTML = newAnime[i].name
            let rat = document.createElement('p')
            rat.classList.add('p-rating')
            rat.innerHTML = Math.floor(newAnime[i].userRating/newAnime[i].peopleRated *100)/100
            txt.append(p)
            txt.append(rat)
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



export function popularityRatings(anime) {
    let newAnime = []
    for(let key in anime) {
        newAnime.push(anime[key])
    }

    newAnime.sort((a, b) => b.members - a.members)
    console.log(newAnime)

    let images = document.querySelector('.images')

    let imgHolder = document.createElement('div')
    imgHolder.classList.add('img-holder')
    images.append(imgHolder)


    for(let i = 0; i< 48; i++) {

        let imgWrapper = document.createElement('div')
        imgWrapper.classList.add('image-wrapper')

        let rating = document.createElement('p')
        rating.classList.add('rating')
        rating.innerHTML = Math.floor(newAnime[i].userRating/newAnime[i].peopleRated *100)/100

        let position = document.createElement('p')
        position.classList.add('position')
        position.innerHTML = i+1

        let difference = document.createElement('p')
        difference.innerHTML = Math.floor((rating.innerHTML-newAnime[i].rating) * 100)/100
        difference.classList.add('difference')

        if(difference.innerHTML > 0.05) difference.classList.add('positive')
        if(difference.innerHTML < -0.4) difference.classList.add('negative')
        if(difference.innerHTML > -0.4 && difference.innerHTML < 0.05) difference.classList.add('neutral')

        console.log(`${i+1}.`,newAnime[i].name, `${rating.innerHTML}`)

        if(i%8 == 0) {
            imgHolder = document.createElement('div')
            imgHolder.classList.add('img-holder')
            images.append(imgHolder)
        }

        if(newAnime[i].bigImage) {
            let img = document.createElement('img')
            img.classList.add('image')
            img.src = newAnime[i].bigImage
            imgWrapper.append(img)
            imgWrapper.append(position)
            if(rating.innerHTML%1 == 0) rating.innerHTML += '.0'
            imgWrapper.append(rating)
            imgWrapper.append(difference)
            imgHolder.append(imgWrapper)
        }
        else {
            let txt = document.createElement('div')
            txt.classList.add('text-container')
            let p = document.createElement('p')
            p.classList.add('title')
            p.innerHTML = newAnime[i].name
            let rat = document.createElement('p')
            rat.classList.add('p-rating')
            rat.innerHTML = Math.floor(newAnime[i].userRating/newAnime[i].peopleRated *100)/100
            txt.append(p)
            txt.append(rat)
            imgHolder.append(txt)
        }
    }
}