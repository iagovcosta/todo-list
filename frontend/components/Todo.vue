<template lang="pug">
    div
        div.columns.is-centered
            div.column.is-10-desktop.is-12-mobile.is-10-tablet
                input(type="text", class="input is-medium", placeholder="Insira uma nova tarefa")
        div
            ul.todo-list.todo-list-divider 
                li 
                    span #1
                li
                    span #2
                li
                    span #3
                li
                    span #4
                li
                    span #5
                
</template>

<script>
export default {
    name: "Todo"
}
</script>

<style>
    .todo-list {
        margin-top: 3rem;
    }

    .todo-list li {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }

    .todo-list li span {
        color: white !important;
    }

    .todo-list > li::before,
    .todo-list > li::after {
        content: "";
        display: table;
    }

    .todo-list > li::after {
        clear: both;
    }

    .todo-list-divider {

    }
</style>