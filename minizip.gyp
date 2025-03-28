{
	'variables': {
		'use_system_zlib%': 0
	},
	'targets': [{
		'target_name': 'minizip',
		'type': 'static_library',
		'cflags': [ '-ansi' ],
		'direct_dependent_settings': {
			'include_dirs': [ 
				'.',
				'contrib/minizip',
			],
		},
		'include_dirs': [ '.', ],
		'sources': [
			'contrib/minizip/ioapi.c',
			'contrib/minizip/zip.c',
			'contrib/minizip/unzip.c',
		],
		'conditions': [
			['use_system_zlib==1', {
				'defines': [ 'USE_SYSTEM_ZLIB' ],
				'link_settings': {
					'libraries': [ '-lz' ],
				},
				'direct_dependent_settings': {
					'defines': [ 'USE_SYSTEM_ZLIB' ],
				},
			}, {
				'dependencies': [
					'zlib.gyp:zlib'
				],
			}],
			['OS in "mac ios" and use_system_zlib==1', {
				'link_settings': {
					'libraries': [ '$(SDKROOT)/usr/lib/libz.tbd' ],
					'libraries!': [ '-lz' ],
				},
			}],
			[ 'OS=="win"', {
				'sources': [ 'contrib/minizip/iowin32.c' ]
			},{
				'cflags!': [ '-ansi' ],
			}],
			[ 'OS in "mac ios"', {
				'xcode_settings': {
					'GCC_C_LANGUAGE_STANDARD': 'ansi',
				},
			}],
			[ 'OS in "android mac ios"', {
				'defines': [ 'USE_FILE32API', ],
			}],
		]
	}],
}
