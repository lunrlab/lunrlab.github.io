/* Enhance the existing BibTeX renderer without changing the bibliography. */
(() => {
    'use strict';
    const display = document.getElementById('bibtex_display');
    if (!display) return;

    const input = document.getElementById('publication-search');
    const clear = document.getElementById('clear-search');
    const status = document.getElementById('publication-status');
    const empty = document.getElementById('search-empty');
    const years = document.getElementById('publication-years');
    let entries = [];
    let groups = [];
    let yearLinks = [];

    const normalize = value => value.normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
    const applySearch = () => {
        const query = normalize(input.value.trim());
        const terms = query.split(/\s+/).filter(Boolean);
        let count = 0;
        entries.forEach(({ element, text }) => {
            const matches = terms.every(term => text.includes(term));
            element.hidden = !matches;
            if (matches) count++;
        });
        groups.forEach(group => {
            group.hidden = ![...group.querySelectorAll('.bibtexentry')].some(entry => !entry.hidden);
        });
        yearLinks.forEach(({ link, group }) => { link.hidden = group.hidden; });
        clear.hidden = !input.value;
        empty.hidden = count > 0;
        status.textContent = query
            ? `${count} of ${entries.length} publications match your search`
            : `${entries.length} publications · 2020 onward`;
    };

    const initialize = () => {
        const rendered = [...display.querySelectorAll('.bibtexentry')];
        if (!rendered.length) return false;
        entries = rendered.map(element => ({ element, text: normalize(element.textContent) }));
        groups = [...display.querySelectorAll('.group.year')];
        years.replaceChildren();
        yearLinks = groups.map(group => {
            const heading = group.querySelector('.year-heading .title');
            const link = document.createElement('a');
            link.href = `#${heading.id}`;
            link.textContent = heading.textContent;
            years.append(link);
            return { link, group };
        });
        applySearch();
        return true;
    };

    input.addEventListener('input', () => { if (entries.length) applySearch(); });
    clear.addEventListener('click', () => {
        input.value = '';
        applySearch();
        input.focus();
    });
    // BibTeX loads asynchronously. Observe only DOM insertions, not search visibility changes.
    const observer = new MutationObserver(() => {
        if (initialize()) observer.disconnect();
    });
    if (!initialize()) observer.observe(display, { childList: true, subtree: true });
    window.setTimeout(() => {
        if (entries.length) return;
        status.textContent = 'The publication list could not load. Please refresh, or use the Google Scholar profile.';
    }, 20000);
})();
