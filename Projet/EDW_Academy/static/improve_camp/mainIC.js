const gameForm = document.getElementById('game-form')

const gamesDataBox = document.getElementById('games-data-box')
const gameInput = document.getElementById('games')

const campsDataBox = document.getElementById('camps-data-box')
const campInput = document.getElementById('camps')

const btnBox = document.getElementById('btn-box')
const alertBox = document.getElementById('alert-box')

const campText = document.getElementById('camp-text')
const gameText = document.getElementById('game-text')

const csrf = document.getElementsByName('csrfmiddlewaretoken')

function loaddoc() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            console.log(JSON.parse(xhttp.response))
            const gamesData = JSON.parse(xhttp.response)
            for (let i = 0; i < gamesData['data'].length; i++) {
                console.log(gamesData['data'][i])
                const option = document.createElement('div')
                option.textContent = gamesData['data'][i].name
                option.setAttribute('class', 'item')
                option.setAttribute('data-value', gamesData['data'][i].name)
                gamesDataBox.appendChild(option)
            }
        }
    }
    xhttp.open('GET', '/games-json/', true);
    xhttp.send();
}
loaddoc()

gameInput.addEventListener('change', e => {
    console.log(e.target.value)
    const selectedGame = e.target.value

    alertBox.innerHTML = ""
    campsDataBox.innerHTML = ""
    campText.textContent = "Choose a camp"
    campText.classList.add("default")

    function loadcamps() {
        const xhttp2 = new XMLHttpRequest();
        xhttp2.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) {
                console.log(JSON.parse(xhttp2.response))
                const campsData = JSON.parse(xhttp2.response)
                for (let i = 0; i < campsData['data'].length; i++) {
                    console.log(campsData['data'][i])
                    const option = document.createElement('div')
                    option.textContent = campsData['data'][i].start_date+" "+campsData['data'][i].end_date
                    option.setAttribute('class', 'item')
                    option.setAttribute('data-value', campsData['data'][i].start_date+" "+campsData['data'][i].end_date)
                    campsDataBox.appendChild(option)
                }
            }
        }
        xhttp2.open('GET', /camps-json/ + selectedGame, true);
        xhttp2.send();
    }
    loadcamps()
})

gameForm.addEventListener('submit', e => {
    e.preventDefault()
    console.log('submitted')
})
