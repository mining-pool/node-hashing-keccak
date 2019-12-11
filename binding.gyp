{
    "targets": [
        {
            "target_name": "hashing",
            "sources": [
                "hashing.cpp",

                "keccak.c",

                "sha3/sph_hefty1.c",
                "sha3/sph_fugue.c",
                "sha3/aes_helper.c",
                "sha3/sph_blake.c",
                "sha3/sph_bmw.c",
                "sha3/sph_cubehash.c",
                "sha3/sph_echo.c",
                "sha3/sph_groestl.c",
                "sha3/sph_jh.c",
                "sha3/sph_keccak.c",
                "sha3/sph_luffa.c",
                "sha3/sph_shavite.c",
                "sha3/sph_simd.c",
                "sha3/sph_skein.c",
                "sha3/sph_whirlpool.c",
                "sha3/sph_shabal.c",
                "sha3/sph_ripemd.c",
                "sha3/sph_sha2.c",
                "sha3/sph_sha2big.c",
                "sha3/sph_tiger.c",
                "sha3/hamsi.c",
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
