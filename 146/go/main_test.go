package main

import "testing"

func assertGet(t *testing.T, cache *LRU, key, want int) {
	t.Helper()
	if got := cache.Get(key); got != want {
		t.Errorf("Get(%d) = %d; want %d", key, got, want)
	}
}

func TestLRUCapacityOneReplacesEntry(t *testing.T) {
	cache := NewLRU(1)
	cache.Put(1, 1)
	cache.Put(2, 2)

	assertGet(t, cache, 1, -1)
	assertGet(t, cache, 2, 2)
	cache.Put(3, 3)
	assertGet(t, cache, 2, -1)
	assertGet(t, cache, 3, 3)
}

func TestLRUCapacityOneGetAndUpdate(t *testing.T) {
	cache := NewLRU(1)
	cache.Put(1, 1)
	assertGet(t, cache, 1, 1)
	cache.Put(1, 10)
	assertGet(t, cache, 1, 10)
	cache.Put(2, 2)
	assertGet(t, cache, 1, -1)
	assertGet(t, cache, 2, 2)
}

func TestLRUEvictsLeastRecentlyUsedAfterGet(t *testing.T) {
	cache := NewLRU(2)
	cache.Put(1, 100)
	cache.Put(2, 200)

	assertGet(t, cache, 1, 100) // key 1 becomes most recently used
	cache.Put(3, 300)

	assertGet(t, cache, 2, -1)
	assertGet(t, cache, 1, 100)
	assertGet(t, cache, 3, 300)
}

func TestLRUUpdatingKeyRefreshesRecency(t *testing.T) {
	cache := NewLRU(2)
	cache.Put(1, 10)
	cache.Put(2, 20)

	cache.Put(1, 15) // Updating a key should also make it most recently used.
	cache.Put(3, 30)

	assertGet(t, cache, 2, -1)
	assertGet(t, cache, 1, 15)
	assertGet(t, cache, 3, 30)
}

func TestLRUMissDoesNotRefreshRecency(t *testing.T) {
	cache := NewLRU(2)
	cache.Put(1, 10)
	cache.Put(2, 20)

	assertGet(t, cache, 99, -1)
	cache.Put(3, 30)

	assertGet(t, cache, 1, -1)
	assertGet(t, cache, 2, 20)
	assertGet(t, cache, 3, 30)
}

func TestLRURepeatedUpdatesDoNotIncreaseSize(t *testing.T) {
	cache := NewLRU(2)
	cache.Put(1, 10)
	cache.Put(2, 20)
	cache.Put(1, 11)
	cache.Put(1, 12)

	if got := cache.size; got != 2 {
		t.Fatalf("size = %d; want 2", got)
	}

	cache.Put(3, 30)
	assertGet(t, cache, 2, -1)
	assertGet(t, cache, 1, 12)
}
