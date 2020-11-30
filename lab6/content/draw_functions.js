let cur_page = 1;
let cur_site = "ecowars";
let last_page = false;

function update(){
    fetch(`/load?site=${cur_site}`)
        .then((request)=>{
            document.getElementById('ans').style.backgroundColor = request.ok ? '#616d38' : '#512b2b' ;
            setTimeout(()=>{
                    document.getElementById('ans').style.backgroundColor = '#777777';
                }, 2000);
        })
    }
    function loadEntries() {
        fetch(`/view?site=${cur_site}&page=${cur_page}`)
            .then(resp => resp.json())
            .then(json => {
                const content = document.getElementById('rss-information');
                content.innerHTML = '';

                const entries = json['entries'];
                for (const entry of entries) {
                    content.innerHTML += `<div class="item">
                        <div class="title">${entry[1]}</div>
                        <div class="description">${entry[2]}</div>
                        <a class="link" href="${entry[3]}">${entry[3]}</a>
                    </div>`;
                }
                last_page = entries.length < 5;

                if (!last_page) {
                    drawNextPage();
                }
            });
        }


function switchPage(pageId) {
    cur_page = pageId;
    navigation_btn();
    loadEntries();
}

function navigation_btn(){
    const container = document.getElementById('navigation');
    container.innerHTML = '';
    if (cur_page > 1)
        container.innerHTML += `<button onclick="switchPage(${cur_page-1})" class="butt">Prev</button>`;
    container.innerHTML += `<button class="butt">${cur_page}</button>`;
}
function drawNextPage() {
    const container = document.getElementById('navigation');
    if (!last_page)
        container.innerHTML += `<button onclick="switchPage(${cur_page+1})" class="butt">Next</button>`;
}
function add_rss_url() {
    const container = document.getElementById('rss_url');
    let url = container.value;
    fetch(`/add?url=${url}`)
    .then(response => {
      if (response.ok)
        return response.json();
      else {
          document.getElementById('rss_url').value = '';
          alert("incorrect URL")
      }
    })
    .then(json => {
        cur_site =json['site'];
        switchPage(1);
        document.getElementById('rss_url').value = '';
    })
    .catch((error) => {
      console.log(error)
    });
}




