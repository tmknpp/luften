import { writable } from 'svelte/store';

export const selectedPupil = writable(null);
export const refreshMessagesTrigger = writable(false);

