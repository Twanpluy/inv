<script lang="ts">
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	export let openmodal = false; // Add a prop to indicate whether the modal is open or closed

	function closeModal() {
		openmodal = false;
	}

	function saveOrder() {
		console.log('save order');
		openmodal = false;
	}
</script>

<!-- Open the modal using ID.showModal() method -->
{#if openmodal}
	<section>
		<div id="modal" class="fixed inset-0 flex items-center justify-center bg-opacity-100">
			<div class="bg-white p-8 rounded-lg shadow-lg">
				<form action="POST">
					<input type="text" placeholder="Type here" class="input input-bordered w-full max-w-xs" />
				</form>

				<div class="flex justify-end mt-4 py-4 py-4">
					<button class="btn btn-success px-4 mx-3" on:click={saveOrder}>Save</button>
					<button class="btn btn-error px-4 mx-3" on:click={closeModal}>Close</button>
				</div>
			</div>
		</div>
	</section>
{/if}
