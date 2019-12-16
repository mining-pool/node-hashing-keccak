{
    "targets": [
        {
            "target_name": "hashing",
            "sources": [
                "hashing.cpp",

                "keccak.c",

                "sha3/sph_keccak.c",

            ],
            "include_dirs": [
                "crypto",
            ],
            "cflags_cc": [
                "-std=c++0x"
            ],
        }
    ]
}
