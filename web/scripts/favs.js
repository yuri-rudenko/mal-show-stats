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

        console.log(animeArr)
    })
}
