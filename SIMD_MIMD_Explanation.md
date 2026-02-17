## Q. Explain with suitable diagram SIMD and MIMD architecture.
*(SPPU: March-17 — 6 Marks, April-18 — 6 Marks, Oct-19 — 6 Marks)*

---

### Ans:

**Flynn's Taxonomy** (proposed by Michael J. Flynn, 1966) is the standard classification of parallel computer architectures. It classifies systems based on two factors:
1. **Number of Instruction Streams** — Single or Multiple
2. **Number of Data Streams** — Single or Multiple

This gives four categories:

| | Single Data | Multiple Data |
|---|---|---|
| **Single Instruction** | SISD | **SIMD** |
| **Multiple Instruction** | MISD | **MIMD** |

Parallel computers fall under **SIMD** and **MIMD**.

---

## 1. SIMD – Single Instruction, Multiple Data

In SIMD, there is **one control unit** that fetches and decodes a single instruction and broadcasts it to **all processing elements (PEs)** at the same time. Each PE executes the **same operation** but on its **own local data**. All PEs work in **lockstep** (synchronously), meaning they all start and finish the instruction at the same time. This makes SIMD ideal for **data-parallel** tasks like vector/matrix operations, image processing, etc.

### Architecture Diagram:

<svg viewBox="0 0 520 295" xmlns="http://www.w3.org/2000/svg" font-family="Arial, sans-serif">
  <defs>
    <marker id="arr" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
  <rect x="160" y="20" width="200" height="50" rx="8" fill="#4A90D9" stroke="#2C5F8A" stroke-width="2"/>
  <text x="260" y="42" font-size="13" font-weight="bold" fill="white" text-anchor="middle">Control Unit</text>
  <text x="260" y="58" font-size="10" fill="#E0EDFF" text-anchor="middle">(Single Instruction Stream)</text>
  <line x1="210" y1="70" x2="100" y2="118" stroke="#333" stroke-width="2" marker-end="url(#arr)"/>
  <line x1="260" y1="70" x2="260" y2="118" stroke="#333" stroke-width="2" marker-end="url(#arr)"/>
  <line x1="310" y1="70" x2="420" y2="118" stroke="#333" stroke-width="2" marker-end="url(#arr)"/>
  <text x="260" y="100" font-size="9" fill="#888" text-anchor="middle" font-style="italic">Same Instruction I</text>
  <rect x="40" y="120" width="120" height="42" rx="6" fill="#E8744F" stroke="#B5532E" stroke-width="2"/>
  <text x="100" y="138" font-size="12" font-weight="bold" fill="white" text-anchor="middle">PE 1</text>
  <text x="100" y="153" font-size="9" fill="white" text-anchor="middle">I on D1</text>
  <rect x="200" y="120" width="120" height="42" rx="6" fill="#E8744F" stroke="#B5532E" stroke-width="2"/>
  <text x="260" y="138" font-size="12" font-weight="bold" fill="white" text-anchor="middle">PE 2</text>
  <text x="260" y="153" font-size="9" fill="white" text-anchor="middle">I on D2</text>
  <rect x="360" y="120" width="120" height="42" rx="6" fill="#E8744F" stroke="#B5532E" stroke-width="2"/>
  <text x="420" y="138" font-size="12" font-weight="bold" fill="white" text-anchor="middle">PE N</text>
  <text x="420" y="153" font-size="9" fill="white" text-anchor="middle">I on DN</text>
  <line x1="100" y1="162" x2="100" y2="195" stroke="#333" stroke-width="2" marker-end="url(#arr)"/>
  <line x1="260" y1="162" x2="260" y2="195" stroke="#333" stroke-width="2" marker-end="url(#arr)"/>
  <line x1="420" y1="162" x2="420" y2="195" stroke="#333" stroke-width="2" marker-end="url(#arr)"/>
  <rect x="55" y="198" width="90" height="35" rx="5" fill="#5CB85C" stroke="#3D8B3D" stroke-width="2"/>
  <text x="100" y="220" font-size="11" fill="white" text-anchor="middle">Mem D1</text>
  <rect x="215" y="198" width="90" height="35" rx="5" fill="#5CB85C" stroke="#3D8B3D" stroke-width="2"/>
  <text x="260" y="220" font-size="11" fill="white" text-anchor="middle">Mem D2</text>
  <rect x="375" y="198" width="90" height="35" rx="5" fill="#5CB85C" stroke="#3D8B3D" stroke-width="2"/>
  <text x="420" y="220" font-size="11" fill="white" text-anchor="middle">Mem DN</text>
  <text x="260" y="262" font-size="13" font-weight="bold" text-anchor="middle" fill="#333">Fig: SIMD Architecture</text>
  <text x="260" y="280" font-size="10" text-anchor="middle" fill="#777">1 Instruction → N Processors → N Different Data</text>
</svg>

### Key Points:
- Single CU dispatches **same instruction** to all PEs → **data parallelism**
- Execution is **synchronous** (lockstep)
- **Less hardware & memory** — only one copy of program
- Requires **specialized hardware**
- **Examples:** Illiac IV, CM-2, MasPar MP-1, Intel SSE, GPU, DSP Sharc

---

## 2. MIMD – Multiple Instruction, Multiple Data

In MIMD, **each processor is a complete independent node** — it has its own control unit, its own program counter, and its own local memory. Each processor can execute a **completely different program** on **completely different data**, and they all work **asynchronously** (at their own pace). Processors communicate via a shared bus or message passing network. This makes MIMD the most **flexible and general-purpose** parallel architecture. Most modern parallel systems (multi-core CPUs, clusters) are MIMD.

### Architecture Diagram:

<svg viewBox="0 0 520 310" xmlns="http://www.w3.org/2000/svg" font-family="Arial, sans-serif">
  <rect x="20" y="20" width="140" height="135" rx="8" fill="#FFF3E0" stroke="#E8744F" stroke-width="2"/>
  <text x="90" y="40" font-size="11" font-weight="bold" text-anchor="middle" fill="#B5532E">Node 1</text>
  <rect x="30" y="48" width="120" height="26" rx="4" fill="#4A90D9" stroke="#2C5F8A" stroke-width="1.5"/>
  <text x="90" y="66" font-size="10" fill="white" text-anchor="middle">Control Unit 1</text>
  <rect x="30" y="80" width="120" height="26" rx="4" fill="#E8744F" stroke="#B5532E" stroke-width="1.5"/>
  <text x="90" y="98" font-size="10" fill="white" text-anchor="middle">PE 1 (Prog P1)</text>
  <rect x="30" y="112" width="120" height="26" rx="4" fill="#5CB85C" stroke="#3D8B3D" stroke-width="1.5"/>
  <text x="90" y="130" font-size="10" fill="white" text-anchor="middle">Mem (D1)</text>
  <rect x="190" y="20" width="140" height="135" rx="8" fill="#FFF3E0" stroke="#E8744F" stroke-width="2"/>
  <text x="260" y="40" font-size="11" font-weight="bold" text-anchor="middle" fill="#B5532E">Node 2</text>
  <rect x="200" y="48" width="120" height="26" rx="4" fill="#4A90D9" stroke="#2C5F8A" stroke-width="1.5"/>
  <text x="260" y="66" font-size="10" fill="white" text-anchor="middle">Control Unit 2</text>
  <rect x="200" y="80" width="120" height="26" rx="4" fill="#E8744F" stroke="#B5532E" stroke-width="1.5"/>
  <text x="260" y="98" font-size="10" fill="white" text-anchor="middle">PE 2 (Prog P2)</text>
  <rect x="200" y="112" width="120" height="26" rx="4" fill="#5CB85C" stroke="#3D8B3D" stroke-width="1.5"/>
  <text x="260" y="130" font-size="10" fill="white" text-anchor="middle">Mem (D2)</text>
  <rect x="360" y="20" width="140" height="135" rx="8" fill="#FFF3E0" stroke="#E8744F" stroke-width="2"/>
  <text x="430" y="40" font-size="11" font-weight="bold" text-anchor="middle" fill="#B5532E">Node N</text>
  <rect x="370" y="48" width="120" height="26" rx="4" fill="#4A90D9" stroke="#2C5F8A" stroke-width="1.5"/>
  <text x="430" y="66" font-size="10" fill="white" text-anchor="middle">Control Unit N</text>
  <rect x="370" y="80" width="120" height="26" rx="4" fill="#E8744F" stroke="#B5532E" stroke-width="1.5"/>
  <text x="430" y="98" font-size="10" fill="white" text-anchor="middle">PE N (Prog PN)</text>
  <rect x="370" y="112" width="120" height="26" rx="4" fill="#5CB85C" stroke="#3D8B3D" stroke-width="1.5"/>
  <text x="430" y="130" font-size="10" fill="white" text-anchor="middle">Mem (DN)</text>
  <line x1="90" y1="155" x2="90" y2="200" stroke="#333" stroke-width="2"/>
  <line x1="260" y1="155" x2="260" y2="200" stroke="#333" stroke-width="2"/>
  <line x1="430" y1="155" x2="430" y2="200" stroke="#333" stroke-width="2"/>
  <rect x="50" y="200" width="420" height="38" rx="8" fill="#9B59B6" stroke="#7D3C98" stroke-width="2"/>
  <text x="260" y="224" font-size="12" font-weight="bold" fill="white" text-anchor="middle">Interconnection Network</text>
  <text x="260" y="268" font-size="13" font-weight="bold" text-anchor="middle" fill="#333">Fig: MIMD Architecture</text>
  <text x="260" y="286" font-size="10" text-anchor="middle" fill="#777">N Instructions → N Processors → N Different Data</text>
  <text x="260" y="304" font-size="10" text-anchor="middle" fill="#999" font-style="italic">SPMD variant: Same program on all nodes, different data</text>
</svg>

### Key Points:
- Each PE has **own control unit + program** → **task parallelism**
- Execution is **asynchronous** (independent)
- **More hardware & memory** — program + OS at each node
- Built from **inexpensive commodity components**
- **SPMD** variant: same program, different data (most popular)
- **Examples:** Sun Ultra, IBM SP, multi-core PCs, workstation clusters

---

## 3. SIMD vs MIMD

The key difference is: **SIMD = one instruction, many data (synchronized)** vs **MIMD = many instructions, many data (independent)**.

| Feature | SIMD | MIMD |
|---------|------|------|
| Control Unit | Single (shared) | One per processor |
| Instruction | Same for all PEs | Different per PE |
| Execution | Synchronous | Asynchronous |
| Hardware | Less | More |
| Memory | Less (1 program copy) | More (program at each PE) |
| Architecture | Specialized hardware | Commodity components |
| Best For | Data parallelism | Task parallelism |
| Examples | Illiac IV, SSE, GPU | IBM SP, Clusters, Multi-core |
