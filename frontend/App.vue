<template lang="pug" > 
    section.hero.has-background-black-bis.is-fullheight
        div.hero-body
            div.container
                div.columns.is-vcentered.is-centered.is-mobile
                    div.columns.is-two-thirds
                        div#form
                            h1.title.is-size-2-desktop.is-size-3.mobile.has-text-centered
                                span.has-text-primary My To-do List
                            todo-component
</template>

<script>
import "bulma/css/bulma.css"
import Todo from './components/Todo'

export default {
    name: "App",
    components: {
        "todo-component": Todo
    }
}
</script>

<style> 
    .text-large {
        font-size: 100px;
    }

    html, body {
        height: 100% !important;
    }

    #form {
        border: 5px solid rgb(43, 139, 102);
        padding: 2rem;
        height: 100% !important;
    }

    #form h1 {
        margin-top: 2.5rem;
        margin-bottom: 3.5rem;
    }

    .body {
        font-size: 'Baloo Thambi 2', cursive;
    }
</style>