import Microsoft.Quantum.Diagnostics.*;

operation Main() : (Result, Result, Result) {
    use (q1, q2, q3) = (Qubit(), Qubit(), Qubit());

    H(q1);
    CNOT(q1, q2);
    H(q3);

    DumpMachine();
    let (m1, m2) = (M(q1), M(q2));
    Reset(q1);
    Reset(q2);

    let m3 = M(q3);
    Reset(q3);

    Message("Hello quantum world!");
    return (m1, m2, m3);
}