<template lang="pug">
    div
        div.columns.is-centered
            div.column.is-10-desktop.is-12-mobile.is-10-tablet
                input(type="text", class="input is-medium", placeholder="Insira uma nova tarefa")
            div.column.is-expanded.is-mobile
                button(class="button is-primary is-medium is-fullwidth") Salvar
        div
            ul.todo-list.todo-list-divider 
                li 
                    div.is-flex.is-justified-between
                        //- button(class="button is-primary is-outlined") Done
                        span Tarefa #1
                        span.has-text-warning Done
                li
                    div
                        button(class="button is-primary is-outlined") Done
                        span Tarefa #2
                li
                    div
                        button(class="button is-primary is-outlined") Done
                        span Tarefa #3
                li
                    div
                        button(class="button is-primary is-outlined") Done
                        span Tarefa #4
                li
                    div
                        button(class="button is-primary is-outlined") Done
                        span Tarefa #5
                
</template>

<script>
export default {
    name: "Todo",
    data () {
        return []
    }
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
        color: white;
    
    }

    .todo-list li button ~ span {
        margin-left: 16px;
    
    }

    .todo-list > li::before,
    .todo-list > li::after {
        content: "";
        display: table;
    }

    .todo-list > li::after {
        clear: both;
    }

    .todo-list-divider > li:nth-child(n+2) {
        margin-top: 10px;
        margin-bottom: 10px;
        padding-top: 16px;
        border-top: 1px solid #ccc;
    }

    .is-justified-between {
        justify-content: space-between;
    }
</style>