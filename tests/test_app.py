import pytest


@pytest.mark.asyncio
async def test_app():
    from app import greeting
    result = await greeting()
    assert result == 'Hello'
