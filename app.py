import streamlit as st
import base64

# Set page configuration with a title and icon
st.set_page_config(
    page_title="포켓몬 도감",
    page_icon="./images/monsterball.png"
)

# Custom CSS
st.markdown(
    """
    <style>
    /* Change the title color */
    h1 {
        color: red;
    }
    /* Set maximum height for images */
    img {
        max-height: 200px;
    }
    /* Center align images and text within the expander */
    .streamlit-expanderContent {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    /* Remove the expander toggle button */
    [data-testid="stExpander"] button {
        display: none;
    }
    /* Prevent the expander from collapsing */
    .streamlit-expanderHeader {
        pointer-events: none;
    }
    /* Remove the fullscreen button on images */
    [data-testid="stImage"] button {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the title
st.title("streamlit 포켓몬 도감")
st.markdown("**포켓몬**을 하나씩 추가해서 도감을 채워보세요!")

type_emoji_dict = {
    "노말": "🐾",
    "불꽃": "🔥",
    "물": "💧",
    "풀": "🍃",
    "전기": "⚡",
    "얼음": "❄️",
    "격투": "🥊",
    "독": "☠️",
    "땅": "🌍",
    "비행": "🌈",
    "에스퍼": "🔮",
    "벌레": "🐛",
    "바위": "🪨",
    "고스트": "👻",
    "드래곤": "🐉",
    "악": "😈",
    "강철": "⚙️",
    "페어리": "🧚‍♀️"
}

# Initial list of Pokémon
initial_pokemons = [
    {
        "name": "피카츄",
        "types": ["전기"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/pikachu.webp"
    },
    {
        "name": "누오",
        "types": ["물", "땅"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/nuo.webp"
    },
    {
        "name": "갸라도스",
        "types": ["물", "비행"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/garados.webp"
    },
    {
        "name": "개굴닌자",
        "types": ["물", "악"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/frogninja.webp"
    },
    {
        "name": "루카리오",
        "types": ["격투", "강철"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/lukario.webp"
    },
    {
        "name": "에이스번",
        "types": ["불꽃"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/acebun.webp"
    },
    {
        "name": "이상해씨",
        "types": ["풀", "독"],
        "image_url": "https://i.namu.wiki/i/yxJpUWcHXx2B9FIuQ6ZM2wgNgV_qkCuBHt9cptUWY6_bTHkRITHXaxOahX8aDDDNqGALE8vXtgDOU8tJc5TZesIl579JJicHhAgYs1_jIaod5x5f-LAuceOVXA_51GVLFFt7gcbOEYQSLvdBAqzhsg.webp"
    },
    {
        "name": "리자몽",
        "types": ["불꽃", "비행"],
        "image_url": "https://i.namu.wiki/i/yUjtwGGamd3jjcyX4puQfCNaZqAK9D0hokIGXG6tP_Q9l_H-EgvEhImTVm87MvzxL4_0Hi1Fi4USMj3QNDTlB2ALQ13fmDNvd39k6nDqbpxA7WUA8_ySb8yc28_ys5_4a69h-ftrkXobpZFEtQI5Nw.webp"
    },
    {
        "name": "거북왕",
        "types": ["물"],
        "image_url": "https://i.namu.wiki/i/tTho6rJtNovNtXpZIr6nASVRzjzhbOe1Wz8NQQWl1LNrs8ZrgxUaue18uPOt8uhsjZtuFAu6r9p4n4JZV5kz1Qvv_742SXwwa4DQ0UTy_HI8pEBifRt8U6OJEL3p0xi7266fa_rUq9qlu_taDH-z7A.webp"
    },
    {
        "name": "뮤츠",
        "types": ["에스퍼"],
        "image_url": "https://i.namu.wiki/i/aYtKhkH6IEVyf41tJaS4nYa5GmVAck8WHH2JYvUyNKS6UF1Tfd69J7WHYE2VvjyKZoNWTUIGSEwYy1STVn63JDxXi4zgk-aBDTtjZu73OHsnCd-ewlzhDk9gYjykM5aZvBVm5rxIZMoWC7v1yY1Dnw.webp"
    }
]

# Initialize session state for pokemons if not already done
if 'pokemons' not in st.session_state:
    st.session_state.pokemons = initial_pokemons

# Toggle for autofill
autofill = st.checkbox("예시 데이터로 채우기")

# Example Pokémon data
example_pokemon = {
    "name": "알로라디그다",
    "types": ["땅", "강철"],
    "image_url": "/Users/soundfury37gmail.com/PycharmProjects/streamlitpokemon/images/알로라_디그다.png"
}

# Form for adding a new Pokémon
with st.form(key='add_pokemon_form', clear_on_submit=True):
    new_name = st.text_input('포켓몬 이름', value=example_pokemon["name"] if autofill else "")
    new_types = st.multiselect(
        '포켓몬 속성',
        options=list(type_emoji_dict.keys()),
        default=example_pokemon["types"] if autofill else [],
        max_selections=2
    )
    new_image_file = st.file_uploader('포켓몬 이미지 파일', type=['png', 'jpg', 'jpeg'])
    new_image_url = st.text_input('포켓몬 이미지 URL', value=example_pokemon["image_url"] if autofill and not new_image_file else "")

    submit_button = st.form_submit_button(label='추가')

    if submit_button:
        if new_name and new_types:
            if new_image_file:
                new_image_bytes = new_image_file.read()
                new_image_base64 = base64.b64encode(new_image_bytes).decode('utf-8')
                new_image_url = f"data:image/png;base64,{new_image_base64}"
            new_pokemon = {
                "name": new_name,
                "types": new_types,
                "image_url": new_image_url or "https://via.placeholder.com/150"
            }
            st.session_state.pokemons.append(new_pokemon)
            st.success(f"{new_name}을(를) 성공적으로 추가했습니다!")
            st.experimental_rerun()  # Reload the page to reflect changes
        else:
            st.error("포켓몬 이름과 속성을 입력해주세요.")

# Display the Pokémon in columns
columns = st.columns(3)

for i, pokemon in enumerate(st.session_state.pokemons):
    col = columns[i % 3]
    with col.expander(label=pokemon["name"], expanded=False):
        # Display the Pokémon name
        col.subheader(pokemon["name"])

        # Display Pokémon types with emojis
        types_with_emojis = [f"{type_emoji_dict[type_]} {type_}" for type_ in pokemon["types"]]
        col.text(" / ".join(types_with_emojis))

        # Display Pokémon image
        if pokemon["image_url"].startswith("data:image"):
            col.image(pokemon["image_url"], caption=pokemon["name"])
        else:
            col.image(pokemon["image_url"], caption=pokemon["name"])

        # Add delete button
        if col.button('삭제', key=f"delete_{i}"):
            del st.session_state.pokemons[i]
            st.experimental_rerun()  # Reload the page to reflect changes
