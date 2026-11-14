---
name: manning-packt-udemy-polyglot-engineering
description: Compact Team Playbook distilled from 2,144 Manning ("100 Java/Go/C++/SQL Mistakes", System Design), Packt, and Udemy courses in ChronicleRAG (<9KB). Enforces polyglot concurrency, memory, SQL sargability, Kafka outbox, and container hardening rules.
---

# Manning, Packt & Udemy Polyglot Production Playbook (`2,144` Books & Courses)

> **Source Corpus**: `167` Manning books (`100 Java/Go/C++/SQL Mistakes`, `Acing System Design`, `Advanced Algorithms`), `63` Packt courses/repos, and `1,914` Udemy courses in `ChronicleRAG`.

## 1. Java 21 & Spring Boot 3 Rules (`context-assistant`, `InsightCV`, Enterprise APIs)
- **Virtual Thread Pinning Guard**: Never execute blocking socket/JDBC I/O inside `synchronized` blocks on Java 21+ Virtual Threads; replace intrinsic monitors with `ReentrantLock`.
- **Bounded Async Composition**: Never call `.join()` / `.get()` without `.orTimeout(budget, TimeUnit.SECONDS)` on `CompletableFuture` pipelines; propagate `MDC` trace IDs explicitly across executors.
- **Exact Monetary & Decimal Math**: Never construct `new BigDecimal(double)` (`0.1` binary float drift); always use `new BigDecimal(String)` or integer minor units (`cents`) for AT `SAF-T`/`ATCUD` calculations.
- **JPA / Hibernate N+1 Prevention**: Ban lazy collection traversal inside serialization loops; use explicit `JOIN FETCH`, `@EntityGraph`, or projection `record` DTOs.

## 2. Go & Rust Systems Concurrency Rules (`SetMiddle` Daemons, Rust Cores)
- **Go Slice Backing-Array Leak Guard**: When slicing a small header/token out of a large read buffer, clone it (`slices.Clone(buf[:n])`) so GC can reclaim the underlying megabyte array.
- **Structured Goroutine Lifecycle**: Every background goroutine must accept `ctx context.Context`, select on `<-ctx.Done()`, and run under `errgroup.Group` with bounded concurrency (`SetLimit`).
- **Rust Async Lock Discipline (`SAST-21` / `CWE-833`)**: Never hold a synchronous `std::sync::MutexGuard` across an `.await` suspension point (deadlocks multi-threaded Tokio executors); scope the guard inside `{ ... }` before `.await` or use `tokio::sync::Mutex`.

## 3. C++20/23 & Embedded Firmware Rules (`CLionProjects`, `CitySocket`, `ESP32`)
- **Zero-Copy Bounds Safety**: Pass contiguous buffers via `std::span<const uint8_t>` instead of raw `(ptr, len)` pairs; validate frame lengths before struct unpacking.
- **Deterministic RAII & ISR Discipline**: Delete copy constructors on hardware peripheral handles; ban heap allocation (`new`/`malloc`) and blocking waits inside interrupt service routines (`ISR`).

## 4. PostgreSQL 17 (`pgvector` + `Apache AGE` + `TimescaleDB`) & SQL Sargability
- **Preserve Index Sargability**: Never wrap indexed columns in functions (`WHERE LOWER(email) = $1` or `WHERE DATE(created_at) = $1`) unless a matching functional index exists; rewrite date filters as half-open intervals (`created_at >= $1 AND created_at < $2`).
- **Keyset Pagination Over `OFFSET`**: On tables `> 10k` rows, replace `OFFSET N LIMIT K` ($O(N)$ scan) with seek predicates `(created_at, id) < ($last_ts, $last_id) ORDER BY created_at DESC, id DESC LIMIT K`.
- **Parameterized Queries Only (`CWE-89`)**: Bind all runtime values via `$1` / `:param` placeholders; validate dynamic `ORDER BY` column names against a strict frozen allowlist.

## 5. Event-Driven Microservices, React 19 & Container Hardening
- **Transactional Outbox + Idempotency Key**: Commit domain state + outbox message in a single ACID transaction and deduplicate consumers by `(consumer_group, event_id)`.
- **React 19 Frontend Hygiene (`InsightUIUX v1.2.0`)**: Parallelize independent fetches (`Promise.all`), compute derived values during render instead of `useEffect` state mirrors, and pass `AbortController.signal` to cancel stale requests on tab/filter switches.
- **Multi-Stage Rootless Containers**: Pin base image digests, drop Linux capabilities (`cap_drop: [ALL]`), run as non-root UID (`USER 10001`), and verify CycloneDX 1.5 SBOM + SARIF 2.1.0 (`RULE-11`).
