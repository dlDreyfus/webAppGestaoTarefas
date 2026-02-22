document.addEventListener('DOMContentLoaded', function () {
    const toggles = document.querySelectorAll('.group-toggle');

    // Evita erro global em páginas sem a tabela de tarefas.
    if (!toggles.length) {
        return;
    }

    toggles.forEach(function (toggle) {
        const groupId = toggle.getAttribute('data-group-target');
        if (!groupId) {
            return;
        }

        const rows = document.querySelectorAll('tr[data-group-id="' + groupId + '"]');
        if (!rows.length) {
            return;
        }

        // Sincroniza o estado inicial entre aria-expanded e visibilidade das linhas.
        const startsExpanded = toggle.getAttribute('aria-expanded') === 'true';
        rows.forEach(function (row) {
            row.classList.toggle('hidden-row', !startsExpanded);
        });

        toggle.addEventListener('click', function () {
            const isExpanded = this.getAttribute('aria-expanded') === 'true';
            const nextExpanded = !isExpanded;

            rows.forEach(function (row) {
                row.classList.toggle('hidden-row', !nextExpanded);
            });

            this.setAttribute('aria-expanded', nextExpanded ? 'true' : 'false');
            this.setAttribute('aria-label', nextExpanded ? 'Recolher grupo' : 'Expandir grupo');
        });
    });
});
