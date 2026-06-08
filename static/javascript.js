document.addEventListener('DOMContentLoaded', () => {
	const form = document.querySelector('form.kontaktform');
	const statusDiv = document.getElementById('statusMessage');

	const params = new URLSearchParams(window.location.search);
	if (params.get('status') === 'sended' && statusDiv) {
		statusDiv.textContent = 'sended';
	}

	if (!form) return;

	form.addEventListener('submit', async (e) => {
		e.preventDefault();

		const formData = new FormData(form);
		const plain = Object.fromEntries(formData.entries());

		console.log('Odesílám formulář (form-data):', plain);

		try {
			const resp = await fetch('/kontakt', {
				method: 'POST',
				body: formData,
			});

			if (resp.ok) {
				const newUrl = window.location.pathname + '?status=sent';
				history.replaceState(null, '', newUrl);
				if (statusDiv) statusDiv.textContent = 'Odesláno';
				form.reset();
				console.log('Formulář odeslán — server odpověděl OK');
			} else {
				console.error('Chyba serveru při odeslání formuláře', resp.status);
			}
		} catch (err) {
			console.error('Chyba při odesílání formuláře', err);
		}
	});
});

